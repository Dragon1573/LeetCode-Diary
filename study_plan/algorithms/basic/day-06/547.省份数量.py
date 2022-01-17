#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#
# https://leetcode-cn.com/problems/number-of-provinces/description/
#
# algorithms
# Medium (61.91%)
# Likes:    693
# Dislikes: 0
# Total Accepted:    180.6K
# Total Submissions: 291.8K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
#
#
# 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c
# 间接相连。
#
# 省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
#
# 给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而
# isConnected[i][j] = 0 表示二者不直接相连。
#
# 返回矩阵中 省份 的数量。
#
#
#
# 示例 1：
#
#
# 输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# 输出：2
#
#
# 示例 2：
#
#
# 输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# 输出：3
#
#
#
#
# 提示：
#
#
# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] 为 1 或 0
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]
#
#
#
# 时间复杂度：O(n^2)，最坏情况下，我们需要遍历整个邻接矩阵
# 空间复杂度：O(n)，最坏情况下，队列可能存储所有节点
from collections import deque
from typing import List


# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # 根据题目要求，给出的邻接矩阵一定是方阵
        R = len(isConnected)
        result = 0

        def bfs(r: int) -> None:
            """ 广度优先搜索 """
            queue = deque()
            queue.append(r)
            while queue:
                x = queue.popleft()
                # 移除当前节点
                isConnected[x][x] = 0
                for y in range(R):
                    # 扫描与其相连的节点
                    if isConnected[x][y] == 1:
                        # 无向图是对称矩阵，需要双向移除
                        isConnected[x][y], isConnected[y][x] = 0, 0
                        # 添加下一个节点
                        queue.append(y)

        for r in range(R):
            if isConnected[r][r] == 1:
                result += 1
                bfs(r)
        return result


# @lc code=end
