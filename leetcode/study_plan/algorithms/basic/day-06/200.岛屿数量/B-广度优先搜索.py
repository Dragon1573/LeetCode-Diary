#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (56.48%)
# Likes:    1502
# Dislikes: 0
# Total Accepted:    380.6K
# Total Submissions: 673.2K
# Testcase Example:  """[["1", "1", "1", "1", "0"],
#                        ["1", "1", "0", "1", "0"],
#                        ["1", "1", "0", "0", "0"],
#                        ["0", "0", "0", "0", "0"]]"""
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
#
#
#
# 示例 1：
#
#
# 输入：grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# 输出：1
#
#
# 示例 2：
#
#
# 输入：grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# 输出：3
#
#
#
#
# 提示：
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] 的值为 '0' 或 '1'
#
#
#
# 时间复杂度：O(MN)
# 空间复杂度：O(min(M, N))，当全是陆地时队列能达到的最大长度
from collections import deque
from typing import List


# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(grid: List[List[str]], row: int, col: int, R: int,
                C: int) -> None:
            """ 广度优先搜索 """
            grid[row][col] = '0'
            queue = deque()
            queue.append((row, col))
            while queue:
                # 弹出当前陆地块
                r, c = queue.popleft()
                # 让已遍历的陆地沉没，防止重复计算
                for nr, nc in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                    if 0 <= r + nr < R and 0 <= c + nc < C:
                        if grid[r + nr][c + nc] == '1':
                            queue.append((r + nr, c + nc))
                            grid[r + nr][c + nc] = '0'

        result, R, C = 0, len(grid), len(grid[0])
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    result += 1
                    bfs(grid, r, c, R, C)
        return result


# @lc code=end
