"""
# HJ60 - 查找组成一个偶数最接近的两个素数

时间限制：C/C++ 1秒，其他 2秒
空间限制：C/C++ 32MB，其他 64MB

## 描述

任意一个偶数（大于2）都可以由2个素数组成，组成偶数的2个素数有很多种情况，
本题目要求输出组成指定偶数的两个素数差值最小的素数对。

本题含有多组样例输入。

数据范围：输入的数据满足 4 <= n <= 1000

## 输出描述

输出两个素数

## 示例

输入：20
输出：
    7
    13

输入：4
输出：
    2
    2
"""
from sys import stdin
from math import sqrt


def isPrime(n: int) -> bool:
    for _ in range(2, int(sqrt(n)) + 1):
        if n % _ == 0:
            return False
    return True


for line in stdin:
    n = int(line)
    for _ in range(n // 2, 1, -1):
        if isPrime(_) and isPrime(n - _):
            print(_, n - _, sep='\n')
            break
    pass
