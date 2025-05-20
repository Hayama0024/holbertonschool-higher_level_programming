#!/usr/bin/python3


class Square:
    def __init__(self, size=0):
        self.size = size  # セッター経由でサイズを設定

    @property
    def size(self):
        return self.__size  # プライベート変数 __size を返す

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")  # 型チェック
        if value < 0:
            raise ValueError("size must be >= 0")       # 範囲チェック
        self.__size = value  # OKなら保存

    def area(self):
        return self.__size ** 2  # 面積 = size × size

    def my_print(self):
        if self.__size == 0:
            print()  # 空行だけ出力
            return
        for _ in range(self.__size):         # 行数分ループ
            print("#" * self.__size)         # "#"を size 個並べて出力
