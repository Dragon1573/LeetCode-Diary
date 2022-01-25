""" HJ97 - 记负均正

# 描述

首先输入要输入的整数个数 n ，然后输入 n 个整数。
输出为 n 个整数中负数的个数，和所有正整数的平均值，结果保留一位小数。

0 即不是正整数，也不是负数，不计入计算。

数据范围： 1 <= n <= 2000 ，输入的整数都满足 |val| <= 1000

# 输入描述

本题有多组输入用例。首先输入一个正整数 n ，然后输入 n 个整数。

# 输出描述

输出负数的个数，和所有正整数的平均值。

# 示例

输入：
    5
    1 2 3 4 5
    10
    1 2 3 4 5 6 7 8 9 0
输出：
    0 3.0
    0 5.0

输入：
    3
    0 0 0
输出：0 0.0
"""

while True:
    try:
        n, array = int(input()), map(int, input().split())
        count, total = [0, 0], 0
        for _ in array:
            if _ < 0:
                count[0] += 1
            elif _ > 0:
                count[1] += 1
                total += _
        print('%d %.1f' % (count[0], (total / count[1])))
    except Exception:
        break
