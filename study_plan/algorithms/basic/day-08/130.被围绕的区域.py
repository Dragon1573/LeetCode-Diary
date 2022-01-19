#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
# https://leetcode-cn.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (45.02%)
# Likes:    707
# Dislikes: 0
# Total Accepted:    147.1K
# Total Submissions: 326.8K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X'
# 填充。
#
#
#
#
# 示例 1：
#
#
# 输入：board =
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# 解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O'
# 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
#
#
# 示例 2：
#
#
# 输入：board = [["X"]]
# 输出：[["X"]]
#
#
#
#
# 提示：
#
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] 为 'X' 或 'O'
#
#
#
#
# 广度优先遍历
from collections import deque
from typing import Deque, List, Tuple


# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            # 空矩阵
            return
        N, M = len(board), len(board[0])
        q: Deque[Tuple[int, int]] = deque()
        """ 扫描四个边界 """
        for i in range(N):
            if board[i][0] == "O":
                q.append((i, 0))
                board[i][0] = "A"
            if board[i][M - 1] == "O":
                q.append((i, M - 1))
                board[i][M - 1] = "A"
        for i in range(M - 1):
            if board[0][i] == "O":
                q.append((0, i))
                board[0][i] = "A"
            if board[N - 1][i] == "O":
                q.append((N - 1, i))
                board[N - 1][i] = "A"
        """ 深度优先标记与边界相邻的区域 """
        while q:
            x, y = q.popleft()
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= mx < N and 0 <= my < M and board[mx][my] == "O":
                    q.append((mx, my))
                    board[mx][my] = "A"
        """ 还原矩阵 """
        for i in range(N):
            for j in range(M):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"


# @lc code=end
