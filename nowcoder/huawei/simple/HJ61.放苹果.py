""" HJ61 - 放苹果

## 描述

把 m 个同样的苹果放在n个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？（用K表示）
[5, 5, 1] 和 [1, 5, 1] 是同一种分法。

数据范围：0 <= m <= 10, 1 <= n <= 10 。

本题含有多组样例输入。

## 输入 & 输出

输入两个 int 整数，输出一个 int 整数

## 示例

输入：7 3
输出：8
"""
from sys import stdin


def placeInto(prev: int, count: int, plate: int) -> int:
    """ 递归计算放置数量

    (param) prev:
        上一个盘子放置的苹果数量（确保后续每个盘子的苹果数量不少于前面）
    (param) count:
        剩余的苹果数量
    (param) plate:
        盘子序号
    """
    if plate == 1:
        # 只有一个盘子的时候，只有唯一的放法
        return 1
    elif plate == 2:
        # 当只有两个盘子的时候，在确保后一个盘子的数量不少于前一个的情况下，
        # 前一个盘子的苹果数量不少于更前一个盘子的数量，
        # 但也不多于剩余苹果数量的一半（起到去重作用）
        return count // 2 + 1 - prev
    else:
        # 当前这个盘子的数量不能少于前一个盘子的数量，
        # 但不能多于将苹果平分到剩余所有盘子的数量
        # （起到去重作用）
        this_max, result = count // plate, 0
        for _ in range(prev, this_max + 1):
            # 根据当前盘子放置的苹果数量，累计后面所有盘子的放置方法数量
            result += placeInto(_, count - _, plate - 1)
        return result


for line in stdin:
    m, n = map(int, line.split(' '))
    print(placeInto(0, m, n))
