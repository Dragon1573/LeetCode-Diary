#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (63.37%)
# Likes:    724
# Dislikes: 0
# Total Accepted:    159K
# Total Submissions: 251.1K
# Testcase Example:  '[1,2,2]'
#
# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
#
#
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
#
#
# 示例 2：
#
#
# 输入：nums = [0]
# 输出：[[],[0]]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
#
#
#
#
#
from typing import Dict, List
from collections import Counter


# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 由于解集中的所有子集可以乱序，因此排序保证输入有序会有好处
        nums.sort()
        # 统计词频，方便分别生成子集
        counter = Counter(nums)

        def handle(c: Dict[int, int]) -> List[List[int]]:
            if not c:
                return [[]]
            k, v = c.popitem()
            head_repeat = [[k] * _ for _ in range(v + 1)]
            tail_repeat = handle(c)
            return [a + b for a in head_repeat for b in tail_repeat]

        return handle(counter)


# @lc code=end
