#!/usr/bin/python3
# 102-magic_calculation.py


def magic_calculation(a, b, c):
    """Mats Fuc bytecode provided by Holberton School."""
    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b - c)
