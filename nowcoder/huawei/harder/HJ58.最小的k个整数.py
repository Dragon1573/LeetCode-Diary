""" HJ58 - 输入n个整数，输出其中最小的k个

# 描述

输入n个整数，输出其中最小的k个整数并按升序输出。

本题有多组输入样例。

输入范围：
    整数个数 1 <= n <= 1000
    数值 1 <= val <= 10000

# 输入描述

第一行输入两个整数n和k，第二行输入一个整数数组。

# 输出描述

输出一个从小到大排序的整数数组。

# 示例

输入：
5 2
1 3 5 7 2
输出：1 2
"""
try:
    while True:
        n, k = map(int, input().strip().split())
        array = [int(_) for _ in input().strip().split()]
        array.sort()
        print(*array[:k])
except Exception:
    pass
