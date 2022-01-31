""" HJ105 - 计负均正Ⅱ

# 描述

输入 n 个整型数，统计其中的负数个数并求所有非负数的平均值，结果保留一位小数，
如果没有非负数，则平均值为0。本题有多组输入数据，输入到文件末尾。

数据范围：1 <= n <= 5000 ，每个数 |val| <= 10**6

# 输入描述

输入任意个整数，每行一个

# 示例

输入：
    -13
    -4
    -7
输出：
    3
    0.0

输入：
    -12
    1
    2
输出：
    1
    1.5
"""
from sys import stdin

array = [0, 0, 0]

for line in stdin:
    n = int(line)
    if n >= 0:
        array[1] += n
        array[2] += 1
    else:
        array[0] += 1

if array[2] == 0:
    temp = 0
else:
    temp = array[1] / array[2]
print('%d\n%.1f' % (array[0], temp))
