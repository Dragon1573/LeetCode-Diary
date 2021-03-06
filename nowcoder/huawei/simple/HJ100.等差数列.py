""" HJ100 - 等差数列

# 描述

给定等差数列 2, 5, 8, 11, 14, ... ，即首项为 2 、公差为 3 的等差数列，输出求等差数列前 n 项和。

本题有多组输入。

数据范围： 1 <= n <= 1000

# 示例

输入：2
输出：7
说明：2 + 5 = 7

输入：275
输出：113575
说明：2 + 5 + ... + 821 + 824 = 113575
"""
from sys import stdin

for line in stdin:
    n = int(line)
    # 等差数列求和公式
    print(2 * n + 3 * n * (n - 1) // 2)
