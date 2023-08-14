#!/usr/bin/python3

if __name__ == "__main__":
    """this Function Print the number of and list of arguments."""
    import sys

    myC = len(sys.argv) - 1
    if myC == 0:
        print("0 arguments.")
    elif myC == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(myC))
    for i in range(myC):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
