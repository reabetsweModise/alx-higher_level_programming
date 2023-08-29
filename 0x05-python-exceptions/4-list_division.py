#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """this Fuction Divides two element by element.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        A new list of length containing all the divisions.
    """
    NewList = []
    for o in range(0, list_length):
        try:
            div = my_list_1[o] / my_list_2[o]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            NewList.append(div)
    return (NewList)

