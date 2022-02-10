""" 花圃种植

难度：简单      答题时长：10分钟

# 描述

给定一个已预先种植少量花束的花圃，以及需要补种的花束数量，判断能否顺利完成补种。

# 说明

相邻的花束会因为争夺土壤营养而死亡，花圃以一维数组的形式提供，1 表示已种植，0
表示未种植。

输入用例满足以上条件。

# 数据范围

1 <= len(flowerbed), n <= 20000

# 示例

输入：[1, 0, 0, 0, 1], 2
输出：False
说明：花圃中最多只能补种 1 株花

输入：[0, 0, 0, 1, 0, 1], 1
输出：True
"""
from typing import List


class Solution(object):
    def canPlaceOn(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        if flowerbed[:3] == [0, 0, 1]:
            count += 1
        if flowerbed[-3:] == [1, 0, 0]:
            count += 1
        size = len(flowerbed)
        for _ in range(size - 3):
            if flowerbed[_:_ + 3] == [0, 0, 0]:
                count += 1
        return n <= count


if __name__ == '__main__':
    s = Solution()
    assert False == s.canPlaceOn([1, 0, 0, 0, 1], 2)
    assert True == s.canPlaceOn([0, 0, 0, 1, 0, 1], 1)
