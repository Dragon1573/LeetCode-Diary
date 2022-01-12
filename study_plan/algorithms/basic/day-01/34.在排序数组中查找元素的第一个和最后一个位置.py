#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (42.29%)
# Likes:    1393
# Dislikes: 0
# Total Accepted:    408.7K
# Total Submissions: 966.5K
# Testcase Example:  '[5, 7, 7, 8, 8, 10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 如果数组中不存在目标值 target，返回 [-1, -1]。
#
# 进阶：
#
#
# 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
#
#
#
#
# 示例 1：
#
#
# 输入：nums = [5, 7, 7, 8, 8, 10], target = 8
# 输出：[3, 4]
#
# 示例 2：
#
#
# 输入：nums = [5, 7, 7, 8, 8, 10], target = 6
# 输出：[-1, -1]
#
# 示例 3：
#
#
# 输入：nums = [], target = 0
# 输出：[-1,-1]
#
#
#
# 提示：
#
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums 是一个非递减数组
# -10^9 <= target <= 10^9
#
#
#
from typing import List


# @lc code=start
class Solution:
    def binarySearch(self, nums: List[int], target: int, lower: bool):
        """ 二分搜索 """
        # 定位边界
        p, r = 0, len(nums)
        q = r - 1
        while p <= q:
            # 获取中间元素
            m = (p + q) // 2
            if nums[m] > target or (lower and nums[m] >= target):
                q, r = m - 1, m
            else:
                p = m + 1
        return r

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 定位左边界
        p = self.binarySearch(nums, target, True)
        # 定位右边界
        q = self.binarySearch(nums, target, False) - 1
        if p <= q and q < len(nums):
            if nums[p] == target and nums[q] == target:
                return [p, q]
        return [-1, -1]


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([], 0))
    print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
    print(s.searchRange([5, 7, 7, 8, 8, 10], 6))
