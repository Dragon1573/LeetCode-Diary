""" HJ80 - 整型数组合并

# 描述

将两个整型数组按照升序合并，并且过滤掉重复数组元素。
输出时相邻两数之间没有空格。
请注意本题有多组样例。

# 输入描述

按下列顺序输入：
1. 输入第一个数组的个数
2. 输入第一个数组的数值
3. 输入第二个数组的个数
4. 输入第二个数组的数值

# 输出描述

输出合并之后的数组

# 示例

输入：
    3
    1 2 5
    4
    -1 0 3 2
输出：-101235
"""
try:
    while True:
        _ = input()
        a = [int(_) for _ in input().strip().split()]
        _ = input()
        b = [int(_) for _ in input().strip().split()]

        array = set(a + b)
        print(*sorted(list(array)), sep='')
except Exception:
    pass
