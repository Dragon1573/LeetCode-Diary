"""
# HJ56 - 完全数计算

时间限制：C/C++ 1秒，其他 2秒
空间限制：C/C++ 32MB，其他 64MB

## 描述

完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。
它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。

例如：28，它有约数1, 2, 4, 7, 14, 28，除去它本身 28 外，
其余 5 个数相加，1 + 2 + 4 + 7 + 14 = 28。

输入 n ，请输出 n 以内（含 n ）完全数的个数。

数据范围：1 <= n <= 5×10^5

本题输入含有多组样例。

## 示例

输入：
    1000
    7
    100
输出：
    3
    1
    2
"""
from sys import stdin
from math import sqrt


def isPerfect(_n: int) -> bool:
    s = 1
    for b in range(2, int(sqrt(_n))):
        if _n % b == 0:
            s += b
            s += _n // b
    return s == _n


for line in stdin:
    n, count = int(line), 0
    for a in range(1, n + 1):
        if isPerfect(a):
            count += 1
    print(count)
