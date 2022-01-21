#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#
# https://leetcode-cn.com/problems/01-matrix/description/
#
# algorithms
# Medium (45.76%)
# Likes:    576
# Dislikes: 0
# Total Accepted:    80.2K
# Total Submissions: 175.3K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。
#
# 两个相邻元素间的距离为 1 。
#
#
#
# 示例 1：
#
#
#
#
# 输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：[[0,0,0],[0,1,0],[0,0,0]]
#
#
# 示例 2：
#
#
#
#
# 输入：mat = [[0,0,0],[0,1,0],[1,1,1]]
# 输出：[[0,0,0],[0,1,0],[1,2,1]]
#
#
#
#
# 提示：
#
#
# m == mat.length
# n == mat[i].length
# 1
# 1
# mat[i][j] is either 0 or 1.
# mat 中至少有一个 0
#
#
#
from typing import List
from collections import deque


# @lc code=start
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        # 构造距离矩阵
        dist = [[0] * n for _ in range(m)]
        # 扫描所有的 0
        zeroes_pos = [(i, j) for i in range(m) for j in range(n)]
        zeroes_pos = [(i, j) for i, j in zeroes_pos if matrix[i][j] == 0]
        # 将所有的 0 添加进初始队列中
        q = deque(zeroes_pos)
        # 记录已经遍历的坐标，防止重复遍历
        seen = set(zeroes_pos)

        # 广度优先搜索
        while q:
            i, j = q.popleft()
            # 遍历四个方向
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
                    seen.add((ni, nj))

        return dist

'charset-normalizer, requests, setuptools, wheel'
# @lc code=end
