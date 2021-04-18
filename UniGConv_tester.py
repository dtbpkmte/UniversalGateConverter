import unittest
import UniGConv


class MyTestCase(unittest.TestCase):
    # Preprocessing tests
    # def test_prep_around_or_operator(self):
    #     self.assertEqual(UniGConv.preprocess("A  + B", "nand"), "A+B")
    #
    # def test_prep_around_nonwords(self):
    #     self.assertEqual(UniGConv.preprocess("A+ (   B ~   C    ) D", "nand"), "A+(B ~C) D")
    #
    # def test_prep_dont_touch_and_operators(self):
    #     self.assertEqual(UniGConv.preprocess("A B ~C D (E F) G", "nand"), "A B ~C D (E F) G")
    # #
    # def test_prep_nor_mode_1(self):
    #     self.assertEqual(UniGConv.preprocess("A B", "nor"), "(A B)")
    #
    # def test_prep_nor_mode_2(self):
    #     self.assertEqual(UniGConv.preprocess("A (B+C)", "nor"), "(A (B+C))")

    # def test_prep_nor_duplicate_paren(self):
    #     self.assertEqual(UniGConv.preprocess("((A B) (C D))", "nor"), "((A B) (C D))")

    # def test_prep_general_1(self):
    #     self.assertEqual(UniGConv.preprocess("A B ~   C D (E +F) G", "nand"), "A B ~C D (E+F) G")
    #
    # def test_prep_general_2(self):
    #     self.assertEqual(UniGConv.preprocess("~B C + A ~C", "nand"), "~B C+A ~C")
    #
    # def test_prep_general_3(self):
    #     self.assertEqual(UniGConv.preprocess("A B ~   C D (E +F) G", "nor"), "(A B ~C D (E+F) G)")
    #
    # def test_prep_general_4(self):
    #     self.assertEqual(UniGConv.preprocess("~B C + A ~C", "nor"), "(~B C)+(A ~C)")
    #
    # def test_prep_general_5(self):
    #     self.assertEqual(UniGConv.preprocess("A+ (   B ~   C    ) D", "nor"), "A+((B ~C) D)")
    #
    # def test_prep_general_6(self):
    #     self.assertEqual(UniGConv.preprocess("A B ~C D (E F) G", "nor"), "(A B ~C D (E F) G)")
    #
    # def test_prep_general_7(self):
    #     self.assertEqual(UniGConv.preprocess("E+(D+H) A (B+C)+~F G", "nor"), "E+((D+H) A (B+C))+(~F G)")

    # deMorgan tests
    def test_deMorgan_nand_1(self):
        self.assertEqual(UniGConv.deMorgan("A+B", "nand"), "~(~A ~B)")

    def test_deMorgan_nand_2(self):
        self.assertEqual(UniGConv.deMorgan("~A+B", "nand"), "~(A ~B)")

    def test_deMorgan_nand_3(self):
        self.assertEqual(UniGConv.deMorgan("~A+~B", "nand"), "~(A B)")

    def test_deMorgan_nand_4(self):
        self.assertEqual(UniGConv.deMorgan("A+B C", "nand"), "~(~A ~(B C))")

    def test_deMorgan_nand_5(self):
        self.assertEqual(UniGConv.deMorgan("A+~(B C)", "nand"), "~(~A B C)")

    def test_deMorgan_nand_6(self):
        self.assertEqual(UniGConv.deMorgan("A+B ~(C ~D)", "nand"), "~(~A ~(B ~(C ~D)))")

    def test_deMorgan_nor_1(self):
        self.assertEqual(UniGConv.deMorgan("A B", "nor"), "~(~A+~B)")

    def test_deMorgan_nor_2(self):
        self.assertEqual(UniGConv.deMorgan("~A B", "nor"), "~(A+~B)")

    def test_deMorgan_nor_3(self):
        self.assertEqual(UniGConv.deMorgan("~A ~B", "nor"), "~(A+B)")

    def test_deMorgan_nor_4(self):
        self.assertEqual(UniGConv.deMorgan("A (B+C)", "nor"), "~(~A+~(B+C))")

    def test_deMorgan_nor_5(self):
        self.assertEqual(UniGConv.deMorgan("A ~(B+C)", "nor"), "~(~A+B+C)")

    def test_deMorgan_nor_6(self):
        self.assertEqual(UniGConv.deMorgan("A B+~(C+~D)", "nor"), "~(~A+~(B+~(C+~D)))")

    def test_deMorgan_nor_7(self):
        self.assertEqual(UniGConv.deMorgan("(~A+~B) (C+~D)", "nor"), "~(~(~A+~B)+~(C+~D))")

    # raw_to_nand & raw_to_nor tests
    # Basics
    def test_basic_nand_1(self):
        self.assertEqual(UniGConv.raw_to_nand("A+B"), "~(~A ~B)")

    def test_basic_nand_2(self):
        self.assertEqual(UniGConv.raw_to_nand("~A+B"), "~(A ~B)")

    def test_basic_nand_3(self):
        self.assertEqual(UniGConv.raw_to_nand("~A+~B"), "~(A B)")

    def test_basic_nand_4(self):
        self.assertEqual(UniGConv.raw_to_nand("A+B C"), "~(~A ~(B C))")

    def test_basic_nand_5(self):
        self.assertEqual(UniGConv.raw_to_nand("A+~(B C)"), "~(~A B C)")

    def test_basic_nand_6(self):
        self.assertEqual(UniGConv.raw_to_nand("A+B ~(C ~D)"), "~(~A ~(B ~(C ~D)))")

    def test_basic_nand_7(self):
        self.assertEqual(UniGConv.raw_to_nand("A ~(B ~(C D))"), "A ~(B ~(C D))")

    def test_basic_nand_8(self):
        self.assertEqual(UniGConv.raw_to_nand("A B+~(C+~D)"), "~(~(A B) ~(~C D))")

    def test_basic_nor_1(self):
        self.assertEqual(UniGConv.raw_to_nor("A B"), "~(~A+~B)")

    def test_basic_nor_2(self):
        self.assertEqual(UniGConv.raw_to_nor("~A B"), "~(A+~B)")

    def test_basic_nor_3(self):
        self.assertEqual(UniGConv.raw_to_nor("~A ~B"), "~(A+B)")

    def test_basic_nor_4(self):
        self.assertEqual(UniGConv.raw_to_nor("A (B+C)"), "~(~A+~(B+C))")

    def test_basic_nor_5(self):
        self.assertEqual(UniGConv.raw_to_nor("A ~(B+C)"), "~(~A+B+C)")

    def test_basic_nor_6(self):
        self.assertEqual(UniGConv.raw_to_nor("A B+~(C+~D)"), "~(~A+~B)+~(C+~D)")

    # No brackets tests
    def test_no_brackets_nand_zero_verbose(self):
        self.assertEqual(UniGConv.raw_to_nand("~B C+A ~C"), "~(~(~B C) ~(A ~C))", "Level 0 Test failed")

    def test_no_brackets_nor_zero_verbose(self):
        self.assertEqual(UniGConv.raw_to_nor("~B C+A ~C"), "~(B+~C)+~(~A+C)", "Level 0 Test failed")

    # Nand redundant parentheses tests
    def test_break_paren_nand_zero_verbose_1(self):
        self.assertEqual(UniGConv.raw_to_nand("A (B C)"), "A B C")

    def test_break_paren_nand_zero_verbose_2(self):
        self.assertEqual(UniGConv.raw_to_nand("(A B C)"), "A B C")

    def test_dont_break_paren_nand_zero_verbose_2(self):
        self.assertEqual(UniGConv.raw_to_nand("~(A B C)"), "~(A B C)")

    def test_break_paren_nor_zero_verbose_1(self):
        self.assertEqual(UniGConv.raw_to_nor("A+(B+C)"), "A+B+C")

    def test_break_paren_nor_zero_verbose_2(self):
        self.assertEqual(UniGConv.raw_to_nor("(A+B+C)"), "A+B+C")

    def test_dont_break_paren_nor_zero_verbose(self):
        self.assertEqual(UniGConv.raw_to_nor("~(A+B+C)"), "~(A+B+C)")

    # Level 2 tests
    def test_level_2_nand_zero_verbose_1(self):
        self.assertEqual(UniGConv.raw_to_nand("A (B+C)"), "A ~(~B ~C)")

    def test_level_2_nand_zero_verbose_2(self):
        self.assertEqual(UniGConv.raw_to_nand("E+(D+H) A"), "~(~E ~(~(~D ~H) A))")

    def test_level_2_nand_zero_verbose_3(self):
        self.assertEqual(UniGConv.raw_to_nand("E+~(D+H) A"), "~(~E ~(~D ~H A))")

    def test_level_2_nand_zero_verbose_4(self):
        self.assertEqual(UniGConv.raw_to_nand("E+~(~D+H) A"), "~(~E ~(D ~H A))")

    def test_level_2_nand_zero_verbose_5(self):
        self.assertEqual(UniGConv.raw_to_nand("E+(D+H) A (B+C)+~F G"),
                         "~(~E ~(~(~D ~H) A ~(~B ~C)) ~(~F G))")

    def test_level_2_nor_zero_verbose_1(self):
        self.assertEqual(UniGConv.raw_to_nor("A (B+C)"), "~(~A+~(B+C))")

    def test_level_2_nor_zero_verbose_2(self):
        self.assertEqual(UniGConv.raw_to_nor("(y+z) (x+~y+~z)"), "~(~(y+z)+~(x+~y+~z))")

    def test_level_2_nor_zero_verbose_3(self):
        self.assertEqual(UniGConv.raw_to_nor("E+~(D+H) A"), "E+~(D+H+~A)")

    def test_level_2_nor_zero_verbose_4(self):
        self.assertEqual(UniGConv.raw_to_nor("E+~(~D+H) A"), "E+~(~D+H+~A)")

    def test_level_2_nor_zero_verbose_5(self):
        self.assertEqual(UniGConv.raw_to_nor("E+(D+H) A (B+C)+~F G"),
                         "E+~(~(D+H)+~A+~(B+C))+~(F+~G)")

    # Level 3 tests
    def test_level_3_nand_zero_verbose_1(self):
        self.assertEqual(UniGConv.raw_to_nand("A B+C (D E+(~A E) (~B+~D))"),
                         "~(~(A B) ~(C ~(~(D E) ~(~A E ~(B D)))))")

    def test_level_3_nor_zero_verbose_1(self):
        self.assertEqual(UniGConv.raw_to_nor("A B+C (D E+(~A E) (~B+~D))"),
                         "~(~A+~B)+~(~C+~(~(~D+~E)+~(A+~E+~(~B+~D))))")


if __name__ == '__main__':
    unittest.main()
