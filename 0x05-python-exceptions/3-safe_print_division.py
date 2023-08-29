#!/usr/bin/python3

def safe_print_division(a, b):
    """ division of a  & b."""
    try:
        D = a / b
    except (TypeError, ZeroDivisionError):
        D = None
    finally:
        print("Inside result: {}".format(D))
    return (D)

