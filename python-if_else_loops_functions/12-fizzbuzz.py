#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101, 1):
        if i % 15 == 0:
            print("FIzzBazz ", end="")
        elif i % 3 == 0:
            print("Fizz ", end="")
        elif i % 5 == 0:
            print("Bazz ", end="")
        else:
            print("{} ".format(i), end="")
