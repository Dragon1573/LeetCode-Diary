""" HJ41 - 称砝码

# 描述

现有一组砝码，重量互不相等，分别为 m_1, m_2, ..., m_n，
每种砝码对应的数量为 x_1, x_2, ..., x_n 。
现在要用这些砝码去称物体的重量（放在同一侧），问能称出多少种不同的重量。


注：称重重量包括 0 。

本题有多组输入！

数据范围：每组输入数据满足 1 <= n <= 10 ， 1 <= m_i <= 2000 ， 1 <= x_i <= 10

# 输入描述

对于每一组测试数据：
    第一行：n 砝码类别数量
    第二行：[m_1, m_2, ..., m_n] 每个砝码的质量
    第三行：[x_1, x_2, ..., x_n] 每种砝码的数量

# 输出描述

利用给定的砝码可以称出的不同的质量数
"""
while True:
    try:
        """ 读取输入 """
        n = int(input())
        weights = [int(_) for _ in input().strip().split()]
        counts = [int(_) for _ in input().strip().split()]
    except Exception:
        break
    else:
        # 生成所有独立的砝码
        array = []
        # 记录所有可能的质量组合（用于去重）
        kinds = set([0])
        # 遍历每种砝码和对应的数量
        for w, c in zip(weights, counts):
            # 扩展砝码数组
            array.extend([w] * c)

        for i in array:
            # 依次从砝码数组中取一个砝码
            for j in list(kinds):
                # 将它放到之前已知的所有组合中，可以组成新的质量组合
                kinds.add(i + j)
        print(len(kinds))
