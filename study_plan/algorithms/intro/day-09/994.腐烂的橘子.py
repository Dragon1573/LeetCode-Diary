#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#
# https://leetcode-cn.com/problems/rotting-oranges/description/
#
# algorithms
# Medium (51.06%)
# Likes:    471
# Dislikes: 0
# Total Accepted:    63.7K
# Total Submissions: 124.8K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# 在给定的网格中，每个单元格可以有以下三个值之一：
#
#
# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
#
#
# 每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
#
# 返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。
#
#
#
# 示例 1：
#
#
#
# 输入：[[2,1,1],[1,1,0],[0,1,1]]
# 输出：4
#
#
# 示例 2：
#
# 输入：[[2,1,1],[0,1,1],[1,0,1]]
# 输出：-1
# 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
#
#
# 示例 3：
#
# 输入：[[0,2]]
# 输出：0
# 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
#
#
#
#
# 提示：
#
#
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] 仅为 0、1 或 2
#
#
#
from typing import List
from collections import deque


# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        # 额外数组记录已经时长
        minutes = [[0] * C for _ in range(R)]
        # 记录腐烂的橘子
        queue = [(r, c) for r in range(R) for c in range(C)]
        queue = [(r, c) for r, c in queue if grid[r][c] == 2]
        # 统计空格数量
        zeros = sum(1 for r in range(R) for c in range(C) if grid[r][c] == 0)
        # 已腐烂的橘子耗时为 0
        for r, c in queue:
            minutes[r][c] = 0
        queue = deque(queue)
        # 记录已访问的格子
        visited = set(queue)
        # 广度优先搜索
        while queue:
            x, y = queue.popleft()
            for a, b in ((x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)):
                if 0 <= a < R and 0 <= b < C:
                    if grid[a][b] and (a, b) not in visited:
                        minutes[a][b] = 1 + minutes[x][y]
                        queue.append((a, b))
                        visited.add((a, b))
        if len(visited) < R * C - zeros:
            # 已访问的橘子数量少于总体橘子数量
            # 表明有橘子未腐烂
            return -1
        else:
            # 否则为总体的最长耗时
            return max(max(row) for row in minutes)


# @lc code=end
