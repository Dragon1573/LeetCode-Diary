""" HJ86 - 求最大连续 bit 数

# 描述

求一个 int 类型数字对应的二进制数字中 1 的最大连续数，例如 3 的二进制为 00000011 ，最大连续 2 个 1 。

本题含有多组样例输入。

数据范围：
    数据组数：1 <= t <= 5
    数值范围：1 <= n <= 500000

进阶：对数时间复杂度、常量空间复杂度

# 示例

输入：
    3
    5
    200
输出：
    2
    1
    2
"""
from sys import stdin

for line in stdin:
    n, count = int(line), 0
    temp = 0
    while n:
        if n & 1:
            temp += 1
        else:
            count = max(temp, count)
            temp = 0
        n >>= 1
    count = max(count, temp)
    print(count)
