#!/usr/bin/python3


def magic_calculation(x, y):
    Result = 0
    for i in range(1, 3):
        try:
            if i > x:
                raise Exception('Too far')
            else:
                Result += x ** y / i
        except:
            Result = y + x
            break
    return (Result)

