from typing import List


def check_valid(board: List[List[int]], x: int, y: int) -> bool:
    """ 合法性校验 """
    # 检查列中的重复值
    for i in range(9):
        if i != x and board[i][y] == board[x][y]:
            return False
    # 检查行中的重复值
    for j in range(9):
        if j != y and board[x][j] == board[x][y]:
            return False
    # 检查宫中的重复值
    m, n = 3 * (x // 3), 3 * (y // 3)
    for i in range(3):
        for j in range(3):
            if (i + m != x or j + n != y):
                if board[i + m][j + n] == board[x][y]:
                    return False
    return True


def dfs(board: List[List[int]]) -> bool:
    """ 深度优先递归穷举 """
    # 遍历扫描数独
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                # 发现空缺单元格
                for k in range(1, 10):
                    # 枚举所有可能的值
                    board[i][j] = k
                    if check_valid(board, i, j) and dfs(board):
                        # 借助短路计算进行剪枝
                        return True
                    # 回溯
                    board[i][j] = 0
                # 都不行，说明上次的数字不合理
                return False
    # 全部便利完，返回True
    return True


while True:
    try:
        board = [[int(a) for a in input().strip().split()] for _ in range(9)]
        dfs(board)
        for _ in board:
            print(*_)
    except Exception:
        break
