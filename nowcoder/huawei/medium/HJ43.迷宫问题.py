""" HJ43 - 迷宫问题

https://www.nowcoder.com/practice/cf24906056f4488c9ddb132f317e03bc
"""
from typing import List

stack = []


def dfs(mat: List[List[int]], r: int, c: int) -> bool:
    n, m = len(mat) - 1, len(mat[0]) - 1
    stack.append((r, c))
    mat[r][c] = 1
    if r == n and c == m:
        return True
    directions = [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]
    for x, y in directions:
        if 0 <= x <= n and 0 <= y <= m and matrix[x][y] == 0:
            if dfs(mat, x, y):
                return True
    stack.pop()
    mat[r][c] = 0
    return False


try:
    while True:
        n, m = map(int, input().split())
        matrix = [[int(x) for x in input().split()] for y in range(n)]

        dfs(matrix, 0, 0)
        for _ in stack:
            print('(%d,%d)' % _)
        stack = []
except Exception:
    pass
