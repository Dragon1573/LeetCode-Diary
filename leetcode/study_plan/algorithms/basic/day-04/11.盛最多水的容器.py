#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
# https://leetcode-cn.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (62.18%)
# Likes:    3105
# Dislikes: 0
# Total Accepted:    607.3K
# Total Submissions: 977.1K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器。
#
#
#
# 示例 1：
#
#
#
#
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
# 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#
# 示例 2：
#
#
# 输入：height = [1,1]
# 输出：1
#
#
# 示例 3：
#
#
# 输入：height = [4,3,2,1,4]
# 输出：16
#
#
# 示例 4：
#
#
# 输入：height = [1,2,1]
# 输出：2
#
#
#
#
# 提示：
#
#
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4
#
#
#
from typing import List


# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        p, q, ans = 0, len(height) - 1, 0
        while p < q:
            """ 在这种情况下才能组成一个合法容器 """
            # 容器宽度由索引差定义，容器高度由更短的垂直线定义
            ans = max(ans, (q - p) * min(height[p], height[q]))
            """ 【提示】
            垂直线越大，容器越高，可能的容积就越大
            我们需要找长度又高、距离又远的两条垂直线
            """
            if height[p] <= height[q]:
                p += 1
            else:
                q -= 1
        return ans


# @lc code=end
