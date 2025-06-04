#!/usr/bin/python3


def read_file(filename=""):
    with open(filename, "r", encording="utf-8") as f:
        content = f.read()
        print(f.read(), end="")
