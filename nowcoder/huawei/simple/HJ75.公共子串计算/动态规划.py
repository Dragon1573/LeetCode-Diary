""" HJ75 - 公共子串计算（动态规划） """


from typing import List


def get_lcs(a: List[str], b: List[str]) -> int:
    # 动态规划矩阵
    dp = [[0] * len(b) for _ in range(2)]
    result = 0
    for i in range(1, len(a)):
        for j in range(len(b)):
            current = 1 if i & 1 == 1 else 0
            previous = 1 if i & 1 == 0 else 0

            # 根据状态转移方程生成矩阵
            if a[i] == b[j]:
                dp[current][j] = dp[previous][j - 1] + 1
                result = max(result, dp[current][j])
            else:
                dp[current][j] = 0
    return result


if __name__ == "__main__":
    x, y = input(), input()
    if len(x) < len(y):
        x, y = y, x
    x, y = [''] + list(x), [''] + list(y)
    print(get_lcs(x, y))
