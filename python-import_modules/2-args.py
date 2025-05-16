#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]  # ファイル名は無視して引数だけ取り出す
    count = len(args)

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print(f"{count} arguments:")

    for i in range(count):
        print(f"{i + 1}: {args[i]}")
