#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
# https://leetcode-cn.com/problems/triangle/description/
#
# algorithms
# Medium (68.31%)
# Likes:    932
# Dislikes: 0
# Total Accepted:    199.2K
# Total Submissions: 291.6K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# 给定一个三角形 triangle ，找出自顶向下的最小路径和。
#
# 每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1
# 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
#
#
#
# 示例 1：
#
#
# 输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# 输出：11
# 解释：如下面简图所示：
# ⁠  2
# ⁠ 3 4
# ⁠6 5 7
# 4 1 8 3
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#
#
# 示例 2：
#
#
# 输入：triangle = [[-10]]
# 输出：-10
#
#
#
#
# 提示：
#
#
# 1
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -10^4
#
#
#
#
# 进阶：
#
#
# 你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？
#
#
#
from typing import List


# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [0] * n
        f[0] = triangle[0][0]

        for i in range(1, n):
            # 每行最右路径只能来自上层最右路径
            f[i] = f[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                # 倒序转移可以压缩中间存储，而不会覆盖上层记录
                # 中间各路径的状态转移方程
                f[j] = min(f[j - 1], f[j]) + triangle[i][j]
            # 每行最左路径只能来自上层最左路径
            f[0] += triangle[i][0]

        return min(f)


# @lc code=end
