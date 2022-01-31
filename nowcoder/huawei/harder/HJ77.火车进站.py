""" HJ77 - 火车进站

# 描述

给定一个正整数 N 代表火车数量，0 < N < 10，接下来输入火车入站的序列，一共 N 辆火车，
每辆火车以数字 1-9 编号，火车站只有一个方向进出，同时停靠在火车站的列车中，
只有后进站的出站了，先进站的才能出站。

要求输出所有火车出站的方案，以字典序排序输出。
数据范围：1 <= n <= 10

进阶：
    时间复杂度 O(n!)
    空间复杂度 O(n)

# 输入描述

有多组测试用例，每一组第一行输入一个正整数 N ，接下来输出 N 行表示出栈顺序

# 输出描述

输出以字典序从小到大排序的火车出站序列号，每个编号以空格隔开，每个输出序列换行。

# 示例

输入：
3
1 2 3
输出：
1 2 3
1 3 2
2 1 3
2 3 1
3 2 1
说明：
    第一种方案：1进、1出、2进、2出、3进、3出
    第二种方案：1进、1出、2进、3进、3出、2出
    第三种方案：1进、2进、2出、1出、3进、3出
    第四种方案：1进、2进、2出、3进、3出、1出
    第五种方案：1进、2进、3进、3出、2出、1出
    请注意， [3, 1, 2] 这个序列是不可能实现的。
"""
from typing import List

result = []


def recurse(wait, stack: List[int], out: List[int]):
    """ 递归求解 """
    if not wait and not stack:
        # 若等待区和编组栈都为空，则产生了一组结果
        result.append(' '.join(map(str, out)))
    if wait:
        # 入栈，此时会快速递归，将所有元素一次性压入栈中
        recurse(wait[1:], stack + [wait[0]], out)
    if stack:
        # 出栈，此时等待区不动，依次从编组栈中弹出
        recurse(wait, stack[:-1], out + [stack[-1]])


try:
    while True:
        n, nums = int(input()), [int(_) for _ in input().split()]
        recurse(nums, [], [])
        print(*sorted(result), sep='\n')
except Exception:
    pass
