#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
#
# https://leetcode-cn.com/problems/shortest-path-in-binary-matrix/description/
#
# algorithms
# Medium (38.11%)
# Likes:    161
# Dislikes: 0
# Total Accepted:    33.7K
# Total Submissions: 88.5K
# Testcase Example:  '[[0, 1], [1, 0]]'
#
# 给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。
#
# 二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n -
# 1)）的路径，该路径同时满足下述要求：
#
#
# 路径途经的所有单元格都的值都是 0 。
# 路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
#
#
# 畅通路径的长度 是该路径途经的单元格总数。
#
#
#
# 示例 1：
#
#
# 输入：grid = [[0, 1], [1, 0]]
# 输出：2
#
#
# 示例 2：
#
#
# 输入：grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
# 输出：4
#
#
# 示例 3：
#
#
# 输入：grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
# 输出：-1
#
#
#
#
# 提示：
#
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] 为 0 或 1
#
#
# DFS 广度优先解法
from collections import deque
from typing import Deque, List, Set, Tuple


# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            # 矩阵仅有一格或左上角不是合法起点
            return -1
        N = len(grid)
        if N == 1:
            return 1
        # 广度优先队列
        q: Deque[Tuple[int, int]] = deque([(0, 0)])
        # 已访问节点集合
        s: Set[Tuple[int, int]] = set([(0, 0)])
        # 当前搜索路径长度
        start = 1
        while q:
            """ 对于每一批次的节点，与起点的距离相同 """
            temp = len(q)
            for _ in range(temp):
                r, c = q.pop()
                """ 扫描与当前节点相邻的 8 个节点 """
                for h, v in ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1),
                             (1, 0), (1, -1), (0, -1)):
                    nh, nv = r + h, c + v
                    # 合法性校验
                    if 0 <= nh < N and 0 <= nv < N and grid[nh][nv] == 0 and (
                            nh, nv) not in s:
                        if nh == N - 1 and nv == N - 1:
                            # 找到了目标节点，直接返回
                            return start + 1
                        # 将目标节点添加到下一批次的搜索队列中
                        q.appendleft((nh, nv))
                        # 访问目标节点的路径是最短的，后续重复访问路径只会更长
                        s.add((nh, nv))
            start += 1
        # 没有合法路径时，距离为无穷远
        return -1


# @lc code=end
