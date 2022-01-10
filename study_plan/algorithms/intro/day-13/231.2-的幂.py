#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#
# https://leetcode-cn.com/problems/power-of-two/description/
#
# algorithms
# Easy (50.47%)
# Likes:    452
# Dislikes: 0
# Total Accepted:    190.6K
# Total Submissions: 377.6K
# Testcase Example:  '1'
#
# 给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
#
# 如果存在一个整数 x 使得 n == 2^x ，则认为 n 是 2 的幂次方。
#
#
#
# 示例 1：
#
#
# 输入：n = 1
# 输出：true
# 解释：2^0 = 1
#
#
# 示例 2：
#
#
# 输入：n = 16
# 输出：true
# 解释：2^4 = 16
#
#
# 示例 3：
#
#
# 输入：n = 3
# 输出：false
#
#
# 示例 4：
#
#
# 输入：n = 4
# 输出：true
#
#
# 示例 5：
#
#
# 输入：n = 5
# 输出：false
#
#
#
#
# 提示：
#
#
# -2^31
#
#
#
#
# 进阶：你能够不使用循环/递归解决此问题吗？
#
#


# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 当且仅当 n 为正整数且 bin(n) 仅有一个 1 时，n 是 2 的幂
        # 获取最低位的 1
        return n > 0 and (n & -n) == n
        # 移除最低位的 1
        # return n > 0 and (n & (n - 1)) == 0


# @lc code=end
