""" HJ68 - 成绩排序

# 描述

输入任意（用户，成绩）序列，可以获得成绩从高到低或从低到高的排列，相同成绩
都按先录入排列在前的规则处理。

注意：
    0 代表从高到低，1 表示从低到高
    本题含有多组输入数据！

数据范围：
    人数 1 <= n <= 200
    数据组数 1 <= t <= 5

进阶：
    时间复杂度 O(n*log(n))
    空间复杂度 O(n)

# 输入描述

输入多行，先输入要排序的人的个数，然后分别输入他们的名字和成绩，以一个空格隔开。

# 输出描述

按照指定方式输出名字和成绩，名字和成绩之间以一个空格隔开。

# 示例

输入：
    3
    0
    fang 90
    yang 50
    ning 70
输出：
    fang 90
    ning 70
    yang 50

输入：
    3
    1
    fang 90
    yang 50
    ning 70
    3
    0
    moolgouua 43
    aebjag 87
    b 67
输出：
    yang 50
    ning 70
    fang 90
    aebjag 87
    b 67
    moolgouua 43
"""
try:
    while True:
        n = int(input())
        flag = int(input())
        array = []
        for _ in range(n):
            name, score = input().strip().split()
            array.append((name, int(score)))
        array.sort(key=lambda _: _[1], reverse=(flag == 0))
        for _ in array:
            print(*_)
except Exception:
    pass
