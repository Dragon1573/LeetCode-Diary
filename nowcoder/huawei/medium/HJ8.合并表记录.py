""" HJ8 - 合并表记录

https://www.nowcoder.com/practice/de044e89123f4a7482bd2b214a685201
"""
from itertools import groupby

if __name__ == '__main__':
    n = int(input())
    # 转换为键值对列表
    array = [[int(x) for x in input().split()] for y in range(n)]

    # MapReduce 词频统计法
    # Python groupby 与 MapReduce 不同，
    # 它只会合并相邻同索引键的项
    array.sort(key=lambda _: _[0])
    array = groupby(array, key=lambda _: _[0])
    array = [[x[0], sum(y[1] for y in x[1])] for x in array]

    for _ in array:
        print(*_)
