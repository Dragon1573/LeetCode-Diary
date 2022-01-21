#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (34.23%)
# Likes:    4190
# Dislikes: 0
# Total Accepted:    762.6K
# Total Submissions: 2.2M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0
# 且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#
#
# 示例 1：
#
#
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#
#
# 示例 2：
#
#
# 输入：nums = []
# 输出：[]
#
#
# 示例 3：
#
#
# 输入：nums = [0]
# 输出：[]
#
#
#
#
# 提示：
#
#
# 0 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
#
#
from typing import List


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n, result = len(nums), []
        # 数组升序排列，可以防止元素出现重复的情况
        # Python 底层以快速排序实现
        nums.sort()
        for a in range(n):
            """ 枚举第一个元素 """
            if a > 0 and nums[a] == nums[a - 1]:
                # 不能出现重复元素
                continue
            c, target = n - 1, -nums[a]
            for b in range(a + 1, n):
                """ 枚举第二个元素 """
                if b > a + 1 and nums[b] == nums[b - 1]:
                    # 不能出现重复元素
                    continue
                while b < c and nums[b] + nums[c] > target:
                    # 确保指针 b 在 c 左侧
                    c -= 1
                if b == c:
                    # 当指针位置重合，后续将不存在 a < b < c 且 sum(a, b, c) == 0 的元素
                    break
                if nums[b] + nums[c] == target:
                    # 满足求和条件
                    result.append([nums[a], nums[b], nums[c]])
        return result


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    assert s.threeSum([]) == []
    assert s.threeSum([0]) == []
    assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
