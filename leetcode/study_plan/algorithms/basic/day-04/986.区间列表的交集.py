#
# @lc app=leetcode.cn id=986 lang=python3
#
# [986] 区间列表的交集
#
# https://leetcode-cn.com/problems/interval-list-intersections/description/
#
# algorithms
# Medium (68.28%)
# Likes:    234
# Dislikes: 0
# Total Accepted:    32.3K
# Total Submissions: 47.3K
# Testcase Example:
# '[[0, 2], [5, 10], [13, 23], [24, 25]]\n'
# '[[1, 5], [8, 12], [15, 24], [25, 26]]'
#
# 给定两个由一些 闭区间 组成的列表，firstList 和 secondList ，其中 firstList[i] = [starti, endi] 而
# secondList[j] = [startj, endj] 。每个区间列表都是成对 不相交 的，并且 已经排序 。
#
# 返回这 两个区间列表的交集 。
#
# 形式上，闭区间 [a, b]（其中 a ）表示实数 x 的集合，而 a  。
#
# 两个闭区间的 交集 是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3] 。
#
#
#
# 示例 1：
#
#
# 输入：firstList = [[0, 2], [5, 10], [13, 23], [24, 25]],
#      secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
# 输出：[[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
#
#
# 示例 2：
#
#
# 输入：firstList = [[1, 3], [5, 9]], secondList = []
# 输出：[]
#
#
# 示例 3：
#
#
# 输入：firstList = [], secondList = [[4, 8], [10, 12]]
# 输出：[]
#
#
# 示例 4：
#
#
# 输入：firstList = [[1, 7]], secondList = [[3, 10]]
# 输出：[[3, 7]]
#
#
#
#
# 提示：
#
#
# 0 <= firstList.length, secondList.length <= 1000
# firstList.length + secondList.length >= 1
# 0 <= start[i] < end[i] <= 10^9
# end[i] < start[i+1]
# 0 <= start[j] < end[j] <= 10^9
# end[j] < start[j+1]
#
#
#
from typing import List


# @lc code=start
class Solution:
    def intervalIntersection(self, firstList: List[List[int]],
                             secondList: List[List[int]]) -> List[List[int]]:
        FIRST_LENGTH, SECOND_LENGTH = len(firstList), len(secondList)
        result, p, q = [], 0, 0
        while p < FIRST_LENGTH and q < SECOND_LENGTH:
            """ 当前位置不超出两个集合的范围 """
            # 获取当前轮次的起止点
            (start_p, end_p), (start_q, end_q) = firstList[p], secondList[q]
            if end_p < start_q:
                # 左区间小于右区间且没有相交
                p += 1
            elif end_q < start_p:
                # 右区间小于左区间且没有相交
                q += 1
            else:
                """ 此种情况下一定有相交区间 """
                # 相交区间的起点为起点的大值
                start_intersection = max(start_p, start_q)
                # 香蕉区间的终点为起点的小值
                end_intersection = min(end_p, end_q)
                result.append([start_intersection, end_intersection])
                if end_p <= end_q:
                    # 左区间更早结束，移动到下一个左区间
                    p += 1
                else:
                    q += 1
        # 后续不可能再有相交区间了
        return result


# @lc code=end
