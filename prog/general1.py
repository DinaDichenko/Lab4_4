#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
напишите программу, которая запрашивает ввод двух значений. 
Если хотя бы одно из них не является числом, то должна выполняться конкатенация,
 т. е. соединение, строк. В остальных случаях введенные числа суммируются.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Box:
    x: str


@dataclass
class Sum:
    def __init__(self, a: Box, b: Box):
        x = a.x
        y = b.x

        if x.isnumeric() and y.isnumeric():
            x = int(x)
            y = int(y)

        self.res = x + y

    def __str__(self):
        return str(self.res)


if __name__ == "__main__":
    a = Box(x=input("Введите первое значение: "))
    b = Box(x=input("Введите второе значение: "))

    print(Sum(a, b))
