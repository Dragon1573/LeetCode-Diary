"""
# HJ15 - 求int型正整数在内存中存储时1的个数

## 描述

输入一个 int 型的正整数，计算出该 int 型数据在内存中存储时 1 的个数。

数据范围：保证在 32 位整型数字范围内

## 示例

输入：5
输出：2

输入：0
输出：0

## 要求

时间：1s    空间：32MB
"""
import sys

mask_2 = 0x55555555
mask_4 = 0x33333333
mask_8 = 0x0F0F0F0F
mask_16 = 0x00FF00FF

for line in sys.stdin:
    x = int(line)
    x = (x & mask_2) + ((x >> 1) & mask_2)
    x = (x & mask_4) + ((x >> 2) & mask_4)
    x = (x & mask_8) + ((x >> 4) & mask_8)
    x = (x & mask_16) + ((x >> 8) & mask_16)
    print((x & 0x0000FFFF) + (x >> 16))
