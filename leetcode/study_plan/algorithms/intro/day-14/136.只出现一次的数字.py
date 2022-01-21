#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
# https://leetcode-cn.com/problems/single-number/description/
#
# algorithms
# Easy (71.92%)
# Likes:    2186
# Dislikes: 0
# Total Accepted:    570.5K
# Total Submissions: 793.1K
# Testcase Example:  '[2,2,1]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 说明：
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 示例 1:
#
# 输入: [2,2,1]
# 输出: 1
#
#
# 示例 2:
#
# 输入: [4,1,2,1,2]
# 输出: 4
#
#
from typing import List
from functools import reduce
from operator import xor


# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # functools.reduce 是规约操作，具有惰性计算特点，能够优化空间占用
        # operator.xor 是位异或运算符
        # 0 ^ x = x, x ^ x = 0, a ^ b ^ a = b ^ (a ^ a) = b ^ 0 = b
        # 由于重复元素最多只出现 2 次，偶数次异或将消除其副作用，
        # 最终仅保留出现 1 次的元素
        return reduce(xor, nums)


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    assert s.singleNumber([2, 2, 1]) == 1
    assert s.singleNumber([4, 1, 2, 1, 2]) == 4
