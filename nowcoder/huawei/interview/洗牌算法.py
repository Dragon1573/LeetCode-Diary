""" 洗牌问题

# 描述

有个长度为 2n 的数组 [a1, a2, ..., an, b1, b2, ..., bn]
希望排序后得到 [a1, b1, a2, b2, ..., an, bn]

请考虑是否存在时间复杂度 O(n) 、空间复杂度 O(1) 的算法
"""
from typing import List


class Solution(object):
    def perfect_shuffle_01(self, array: List[int]) -> None:
        """ 解法一 """
        if len(array) <= 1:
            return
        size = len(array)
        n = size // 2
        for i in range(n, size):
            # 需要交换的元素数量
            count = n - (i - n) - 1
            # 待交换
            index = i
            for j in range(1, count + 1):
                array[index], array[i - j] = array[i - j], array[index]
                index = i - j
