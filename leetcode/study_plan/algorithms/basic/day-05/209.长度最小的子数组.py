#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (47.86%)
# Likes:    894
# Dislikes: 0
# Total Accepted:    239.7K
# Total Submissions: 500.9K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 给定一个含有 n 个正整数的数组和一个正整数 target 。
#
# 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr]
# ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
#
#
#
# 示例 1：
#
#
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
#
#
# 示例 2：
#
#
# 输入：target = 4, nums = [1,4,4]
# 输出：1
#
#
# 示例 3：
#
#
# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0
#
#
#
#
# 提示：
#
#
# 1
# 1
# 1
#
#
#
#
# 进阶：
#
#
# 如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
#
#
#
import bisect
from typing import List


# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 空列表无解
        if not nums:
            return 0
        n = len(nums)
        result = n + 1
        # 计算从列表首元素到当前元素的累计求和
        cumsum = [0]
        for _ in nums:
            cumsum.append(cumsum[-1] + _)
        """ 遍历窗口起始点 """
        for _ in range(1, n + 1):
            # 我们需要查找的元素值
            temp = target + cumsum[_ - 1]
            # 获取插入点，插入点左侧值小于插入值
            bound = bisect.bisect_left(cumsum, temp)
            if bound != len(cumsum):
                # 存在元素求和大于目标值的组合
                result = min(result, bound - (_ - 1))
        # 所有元素的总和仍小于目标值，则返回 0
        return 0 if result == n + 1 else result


# @lc code=end
