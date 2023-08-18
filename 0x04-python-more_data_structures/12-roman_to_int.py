#!/usr/bin/python3
def to_subtract(list_num):
    to_sub = 0
    max_list = max(list_num)

    for k in list_num:
        if max_list > k:
            to_sub += k

    return (max_list - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_n.keys())

    my_num = 0
    lastrom = 0
    listnum = [0]

    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if rom_n.get(ch) <= lastrom:
                    my_num += to_subtract(listnum)
                    listnum = [rom_n.get(ch)]
                else:
                    listnum.append(rom_n.get(ch))

                lastrom = rom_n.get(ch)

    my_num += to_subtract(listnum)

    return my_num

