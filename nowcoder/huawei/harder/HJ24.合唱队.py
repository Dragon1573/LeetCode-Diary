""" HJ24 - 合唱队

题解链接： https://blog.nowcoder.net/n/b1510d9d88624137b42982af6406134c

# 描述

N 位同学站成一排，音乐老师要请其中的 (N - K) 位同学出列，使得剩下的 K 位同学排成合唱队形。

合唱队形是指这样的一种队形：

    设 K 位同学从左到右依次编号为 1, 2, ..., K ，他们的身高分别为 T_1, T_2, ..., T_k ，
    则他们的身高满足存在 i (1 <= i <= K) 使得
    T_1 < T_2 < ... < T_{i - 1} > T_i > T_{i + 1} > ... > T_{k - 1} > T_k

你的任务是，已知所有 N 位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。

【注意】不允许改变队列元素的先后顺序，且不要求最高同学左右人数必须相等。
请注意处理多组输入输出！

数据范围： 1 <= n <= 3000

# 输入描述

有多组用例，每组都包含两行数据，第一行是同学的总数 N ，第二行是 N 位同学的身高，以空格隔开

# 示例

输入：
    8
    186 186 150 200 160 130 197 200
输出：4
说明：由于不允许改变队列元素的先后顺序，所以最终剩下的队列应该为 186 200 160 130 或 150 200 160 130
"""
# 二分查找
from bisect import bisect_left
from typing import List


def hcteam(_: List[int]) -> List[int]:
    """ 寻找最长子序列 """
    # 实际合唱队列，这是一个升序队列
    arr = [_[0]]
    # 动态规划表
    dp = [1] * len(_)
    for i in range(1, len(_)):
        if _[i] > arr[-1]:
            # 若本人比队列所有人高，则添加到队尾
            arr.append(_[i])
            # 本人左侧（含自己）的最多人数就是当前合唱队列总人数
            dp[i] = len(arr)
        else:
            # 否则，二分法查找比本人高的人
            pos = bisect_left(arr, _[i])
            # 交换两人，产生新的合唱队列
            arr[pos] = _[i]
            # 本人左侧（含自己）的人数即为合唱队列中左侧的总人数加上自己
            dp[i] = pos + 1
    return dp


try:
    while True:
        n, array = int(input()), [int(_) for _ in input().split()]
        # 分别获取每个人两侧最多能站多少人
        left_t, right_t = hcteam(array), hcteam(array[::-1])[::-1]
        # 两侧均包含本人，需要去重；获得包含本人在内最多可以形成的队列人数
        res = [left_t[i] + right_t[i] - 1 for i in range(len(array))]
        # 保留最长的队列人数即可剔除最少的人
        print(n - max(res))
except Exception:
    pass
