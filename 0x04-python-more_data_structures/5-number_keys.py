#!/usr/bin/python3
def number_keys(a_dictionary):
    k = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        k += 1

    return k

