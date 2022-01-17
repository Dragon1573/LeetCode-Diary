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
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
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
# 时间复杂度：O(MN * alpha(MN))，其中 alpha 函数为反阿克曼函数，可以认为是一个常数
# 空间复杂度：O(MN)
from typing import List


# @lc code=start
class Solution:
    class UnionFind:
        """ 实现并查集 """
        def __init__(self, grid: List[List[str]]):
            M, N = len(grid), len(grid[0])
            self.count = 0
            # 记录各元素的父节点
            self.parent = [-1] * (M * N)
            # 按秩合并
            self.rank = [0] * (M * N)
            """ 将所有的陆地标记为独立的并查集，其父节点为自身 """
            for i in range(M):
                for j in range(N):
                    if grid[i][j] == '1':
                        self.parent[i * N + j] = i * N + j
                        self.count += 1

        def find(self, i: int) -> int:
            """ 路径压缩算法，并查集内所有节点的父节点统一标记为根节点 """
            if self.parent[i] != i:
                self.parent[i] = self.find(self.parent[i])
            return self.parent[i]

        def union(self, x: int, y: int) -> None:
            """ 合并并查集 """
            root_x, root_y = self.find(x), self.find(y)
            if root_x != root_y:
                if self.rank[root_x] < self.rank[root_y]:
                    root_x, root_y = root_y, root_x
                self.parent[root_y] = root_x
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_y] += 1
                self.count -= 1

        def get_count(self) -> int:
            return self.count

    def numIslands(self, grid: List[List[str]]) -> int:
        n_rows = len(grid)
        if n_rows == 0:
            return 0
        n_cols = len(grid[0])
        uf = self.UnionFind(grid)
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == '1':
                    # 当前陆地已遍历
                    grid[r][c] = '0'
                    """ 扫描相邻陆地 """
                    for x, y in ((r - 1, c), (r + 1, c), (r, c - 1), (r,
                                                                      c + 1)):
                        if 0 <= x < n_rows and 0 <= y < n_cols and grid[r][
                                c] == '1':
                            # 存在相邻陆地，执行并查集合并
                            uf.union(r * n_cols + c, x + n_cols + y)
        return uf.get_count()


# @lc code=end
