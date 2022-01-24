""" HJ83 - 二维数组操作

# 描述

1. 输入 m 和 n ，判断能否初始化表格；
2. 输入 x1, y1, x2, y2 ，判断能否交换两个单元格的值；
3. 输入 x ，判断能否在上方插入一行；
4. 输入 y ，判断能否在左侧插入一列；
5. 输入 x, y ，判断能否查找到相应单元格。

编写程序判断以上操作的合法性。

详细要求：

1. 表格最大为 9 × 9 ，超出范围应返回错误；
2. 插入操作不实际作用于表格；
3. 行列索引从 0 开始。

本题含有多组测试样例！

数据范围：1 <= t <= 5
进阶：常量时间复杂度、常量空间复杂度

# 输出描述

操作成功返回 0 ，否则返回 -1 。
"""
while True:
    try:
        # 问题一
        m, n = map(int, input().split())
        if 1 <= m <= 9 and 1 <= n <= 9:
            print(0)
        else:
            print(-1)

        # 问题二
        x1, y1, x2, y2 = map(int, input().split())
        if 0 <= x1 < m and 0 <= x2 < m and 0 <= y1 < n and 0 <= y2 < n:
            print(0)
        else:
            print(-1)

        # 问题三
        r = int(input())
        if 0 <= r < m and m + 1 <= 9:
            print(0)
        else:
            print(-1)

        # 问题四
        c = int(input())
        if 0 <= c < n and n + 1 <= 9:
            print(0)
        else:
            print(-1)

        # 问题五
        z, w = map(int, input().split())
        if 0 <= z < m and 0 <= w < n:
            print(0)
        else:
            print(-1)
    except Exception:
        break
