"""
# HJ35 - 蛇形矩阵

时间限制：C/C++ 1秒，其他 2秒
空间限制：C/C++ 32MB ，其他 64MB

## 描述

蛇形矩阵是由 1 开始的自然数依次排列成的一个矩阵上三角形。例如，当输入 5 时，应该输出的三角形为：

    1 3 6 10 15
    2 5 9 14
    4 8 13
    7 12
    11

请注意本题含有多组样例输入。

## 示例

输入：4
输出：
    1 3 6 10
    2 5 9
    4 8
    7
"""
from sys import stdin

if __name__ == '__main__':
    # 用这种结构处理多组输入
    for line in stdin:
        N = int(line)
        # 初始化结果矩阵
        result = [[] for _ in range(N)]
        result[0].append(1)
        # 按规律初始化每行首列元素
        for _ in range(1, N):
            result[_].append(result[_ - 1][0] + _)
        # 按规律不断扩充每行元素
        for i in range(2, N + 1):
            for j in range(0, i - 1):
                result[j].append(result[j][-1] + i)
        for _ in result:
            print(' '.join(map(str, _)))
