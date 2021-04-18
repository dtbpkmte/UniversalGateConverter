# UniversalGateConverter
Python script to convert regular logical expressions into NAND/NOR format.

Usage: <code>python UniGConv.py</code>

Note: logical expression should use Logisim format (' ' for AND operator, '+' for OR operator, '~' for NOT operator, and parentheses)

Example input: 
```python 
nor:A (B + C)  # output: ~(~A+~(B+C))
```
