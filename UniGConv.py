"""
    Universal Gate Converter
    Author: Duc Doan
    Version: 1.0 - 04/16/2021

    A script to convert logical expressions in Logisim format into NAND/NOR-only expressions.
    v1.0 - 04/16/2021: support verbose mode 0 - output expression contains AND/OR, NOT, NAND/NOR
                        (not 100% universal gates but human readable)
"""
import re
import sys


def preprocess(r):
    """
    Function to remove all redundant spaces except for those meaning operator AND
    :param r: string : input logical expression
    :return: logical expression removed all redundant spaces
    """
    r = re.sub(r"(?<=[(+~])\s*|\s*(?=[)+])", "", r)  # remove space after/before certain characters
    r = re.sub(r"\s+", " ", r)  # remove other redundant spaces, leaving only 1
    return r


def has_global_paren(exp):
    if exp[:2] == "~(" or exp[0] == '(':
        i = 0
        level = 0
        while i < len(exp):
            if exp[i] == '(':
                level += 1
            elif exp[i] == ')':
                level -= 1
                if level == 0 and i != len(exp) - 1:
                    return False
            i += 1
        return True
    else:
        return False


def conv(r, mode, _verbose=0):
    """
    Wrapper function to convert a logical expression to universal gates format

    :param r:       string : input logic expression containing ~/./+ only
    :param mode:    string : "nand" or "nor"
    :param verbose: int    : 0 : results may include and/or, not, nand/nor (default),
                             1 : results may include not, nand/nor,
                             2 : results only include nand/nor
    :return: the expression in nand/nor format
    """
    if mode == "nand":
        return raw_to_nand(r, _verbose)
    elif mode == "nor":
        return raw_to_nor(r, _verbose)
    else:
        raise Exception("Mode can only be nand or nor")


def raw_to_nand(r, _verbose=0):
    r = preprocess(r)
    r = '(' + r + ')'

    if _verbose == 0:
        i = 0
        i_stack = []  # index stack
        t_stack = []  # sub-expression stack
        inverted = False  # does this sub-expression already have a ~?
        t = ""  # sub-expression
        while i < len(r):
            ch = r[i]
            if ch == '(':
                i_stack.append(i)
                t_stack.append(t)
                t = ""
                if i > 0 and r[i-1] == '~':
                    inverted = True
            elif ch == ')':
                start_index = i_stack.pop()
                t_prev = t_stack.pop()
                # process t
                if '+' not in t:
                    if inverted:
                        pass
                    else:  # break redundant parentheses
                        try:
                            r = r[:start_index] + t + r[i+1:]
                            i -= 2
                        except IndexError:
                            r = r[:start_index] + t
                            # return here?
                else:
                    dm = deMorgan(t, "nand")
                    if start_index == 0:
                        return dm
                    if inverted:
                        r = r[:start_index-1] + dm[2:-1] + r[i+1:]  # invert invert = no invert
                        i += len(dm)-3 - (i - start_index + 1) - 1
                        start_index -= 1  # disregard the ~
                        t_prev = t_prev[:-1]  # disregard the ~
                    else:
                        r = r[:start_index] + dm[:-1] + r[i:]  # do not include opening paren
                        i += len(dm)-1 - (i - start_index)
                t = t_prev + r[start_index:i+1]
            else:
                t += ch
            i += 1
        return r[1:-1] if has_global_paren(r) and r[0] == '(' else r
    else:
        # placeholder
        return ""


def raw_to_nor(r, _verbose=0):
    r = raw_to_nand(r)
    r = '(' + r + ')'

    if _verbose == 0:
        i = 0
        i_stack = []  # index stack
        t_stack = []  # sub-expression stack
        inverted = False  # does this sub-expression already have a ~?
        t = ""  # sub-expression
        while i < len(r):
            ch = r[i]
            if ch == '(':
                i_stack.append(i)
                t_stack.append(t)
                t = ""
                if i > 0 and r[i - 1] == '~':
                    inverted = True
            elif ch == ')':
                start_index = i_stack.pop()
                t_prev = t_stack.pop()
                # process t
                if ' ' not in t:
                    if inverted:
                        pass
                    else:  # break redundant parentheses
                        try:
                            r = r[:start_index] + t + r[i + 1:]
                            i -= 2
                        except IndexError:
                            r = r[:start_index] + t
                            # return here?
                else:
                    dm = deMorgan(t, "nor")
                    if start_index == 0:
                        return dm
                    if inverted:
                        r = r[:start_index - 1] + dm[2:-1] + r[i + 1:]  # invert invert = no invert
                        i += len(dm) - 3 - (i - start_index + 1) - 1
                        start_index -= 1  # disregard the ~
                        t_prev = t_prev[:-1]  # disregard the ~
                    else:
                        r = r[:start_index] + dm[:-1] + r[i:]  # do not include opening paren
                        i += len(dm) - 1 - (i - start_index)
                t = t_prev + r[start_index:i + 1]
            else:
                t += ch
            i += 1
        return r[1:-1] if has_global_paren(r) and r[0] == '(' else r
    else:
        # placeholder
        return ""


def deMorgan(expression, mode):
    """
    Implementation of de Morgan's theorem
    :param expression: string : the logic expression
    :param mode: string : target gate (nand/nor)
    :return: the transformed expression using de Morgan theorem
    """

    res_operands = []
    if mode == "nand":
        operands = expression.split('+')
        for op in operands:
            # if this operand contains more than 1 term
            if ' ' in op:
                if has_global_paren(op):
                    if op[0] == '~':
                        res_operands.append(op[2:-1])
                    else:
                        res_operands.append('~' + op)
                else:
                    res_operands.append('~({})'.format(op))
            else:
                if op[0] == '~':
                    res_operands.append(op[1:])
                else:
                    res_operands.append('~' + op)
        return "~(" + ' '.join(res_operands) + ')'
    elif mode == "nor":
        operands = expression.split(' ')
        for op in operands:
            # if this operand contains more than 1 term
            if '+' in op:
                # TODO: make sure that all operands of + must be parenthesized,
                #  below's just a quick fix and may have bug
                # if op[0] == '~':
                #     res_operands.append(op[2:-1])
                # elif op[0] == '(':
                #     res_operands.append('~'+op)
                # else:
                #     res_operands.append('~({})'.format(op))

                # lazy fix
                if has_global_paren(op):
                    if op[0] == '~':
                        res_operands.append(op[2:-1])
                    else:
                        res_operands.append('~' + op)
                else:
                    res_operands.append('~({})'.format(op))
            else:
                if op[0] == '~':
                    res_operands.append(op[1:])
                else:
                    res_operands.append('~' + op)
        return "~(" + '+'.join(res_operands) + ')'
    else:
        raise Exception("Mode can only be nand or nor")


if __name__ == "__main__":
    verbose = 0

    args = sys.argv[1:]
    if len(args) == 0:
        pass
    elif args[0] == "-v" or args[0] == "--verbose":
        print("Verbose modes other than 0 is not available in this version. Defaulting to 0")
        # verbose = int(args[1])
        verbose = 0
    else:
        raise Exception("Invalid argument")

    print("UniGConv v1.0")
    print("Verbose mode: {}".format(verbose))
    print("Enter [mode]:[expression] to convert, q to quit. Note: [mode] is nand/nor, [expression] is in Logisim format")
    print()

    print("Your command: ")
    ip = input()
    while ip != 'q':
        ip_arr = ip.split(':')
        res = conv(ip_arr[1], ip_arr[0], verbose)
        print("Result: {}".format(res))

        print("\nYour command: ")
        ip = input()
    quit()
