#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (56.84%)
# Likes:    646
# Dislikes: 0
# Total Accepted:    237.9K
# Total Submissions: 418.6K
# Testcase Example:  '[3,4,5,1,2]'
#
# 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7]
# 在变化后可能得到：
#
# 若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
# 若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
#
#
# 注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2],
# ..., a[n-2]] 。
#
# 给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
#
#
#
# 示例 1：
#
#
# 输入：nums = [3,4,5,1,2]
# 输出：1
# 解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。
#
#
# 示例 2：
#
#
# 输入：nums = [4,5,6,7,0,1,2]
# 输出：0
# 解释：原数组为 [0,1,2,4,5,6,7] ，旋转 4 次得到输入数组。
#
#
# 示例 3：
#
#
# 输入：nums = [11,13,15,17]
# 输出：11
# 解释：原数组为 [11,13,15,17] ，旋转 4 次得到输入数组。
#
#
#
#
# 提示：
#
#
# n == nums.length
# 1
# -5000
# nums 中的所有整数 互不相同
# nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转
#
#
#
from typing import List


# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        p, q = 0, len(nums) - 1
        R = q
        while p <= q:
            m = (p + q) // 2
            if p == q:
                # 仅有 1 个元素
                return nums[p]
            elif p + 1 == q:
                # 仅有2个元素
                return nums[p] if nums[p] < nums[q] else nums[q]
            elif nums[m] < nums[m + 1] < nums[m - 1]:
                # 元素小于右侧值小于左侧值，说明当前位置为局部有序分段点，是最小值
                return nums[m]
            elif nums[0] <= nums[m] <= nums[R]:
                # 数组整体升序排列，最小元素为首元素
                return nums[0]
            elif nums[0] <= nums[m - 1]:
                # 数组一侧局部有序，最小值一定在另一侧
                p = m + 1
            else:
                q = m - 1


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    assert s.findMin([3, 4, 5, 1, 2]) == 1
    assert s.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert s.findMin([11, 13, 15, 17]) == 11
    assert s.findMin([5, 6, 1, 3, 4]) == 1
    assert s.findMin([5]) == 5
    assert s.findMin([4, 3]) == 3
    assert s.findMin([2, 3, 1]) == 1
