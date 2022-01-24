""" HJ72 - 百钱买百鸡问题

时间限制：C/C++ 1秒，其他 2秒
空间限制：C/C++ 32MB ，其他 64MB

## 描述

公元五世纪，我国古代数学家张丘建在《算经》一书中提出了『百鸡问题』：

    鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？

现要求你打印出所有花一百元买一百只鸡的方式。

## 输入描述

本题多组案例，对每一组案例输入任何一个整数，即可运行程序。

## 输出描述

输出有数行，每行三个整数，分别代表鸡翁，母鸡，鸡雏的数量。

## 示例

输入：1
输出：
    0 25 75
    4 18 78
    8 11 81
    12 4 84
"""
from sys import stdin

for line in stdin:
    for x in range(21):
        for y in range(34):
            z = 100 - 5 * x - 3 * y
            if x + y + 3 * z == 100:
                print(x, y, 3 * z)
