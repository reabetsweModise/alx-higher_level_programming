#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    listkeys = list(a_dictionary.keys())

    for j in listkeys:
        if value == a_dictionary.get(j):
            del a_dictionary[j]

    return (a_dictionary)

