#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于K的子数组
#
# https://leetcode-cn.com/problems/subarray-product-less-than-k/description/
#
# algorithms
# Medium (42.89%)
# Likes:    328
# Dislikes: 0
# Total Accepted:    31K
# Total Submissions: 72.2K
# Testcase Example:  '[10,5,2,6]\n100'
#
# 给定一个正整数数组 nums和整数 k 。
#
# 请找出该数组内乘积小于 k 的连续的子数组的个数。
#
#
#
# 示例 1:
#
#
# 输入: nums = [10,5,2,6], k = 100
# 输出: 8
# 解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
# 需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
#
#
# 示例 2:
#
#
# 输入: nums = [1,2,3], k = 0
# 输出: 0
#
#
#
# 提示:
#
#
# 1 <= nums.length <= 3 * 10^4
# 1 <= nums[i] <= 1000
# 0 <= k <= 10^6
#
#
#
import bisect
from math import log
from typing import List


# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k) -> int:
        if k == 0:
            # 题目提示所有元素都是正整数，任何正整数乘积都大于 0
            return 0
        # 将数值转换为对数，乘法转换为加法以防止数值溢出
        k = log(k)
        """ 计算从数组开头到当前位置的对数求和 """
        prefix = [0.0]
        for _ in nums:
            prefix.append(prefix[-1] + log(_))
        result = 0
        """ 遍历所有的起始位点 """
        for i, v in enumerate(prefix):
            # 在起始位点之后的位置查找小于目标对数值的插入位点
            j = bisect.bisect(prefix, v + k - 1e-9, i + 1)
            # 从起始位点到终止位点之间的所有可能的元素组合，其乘积都小于目标值
            result += j - i - 1
        return result


# @lc code=end
