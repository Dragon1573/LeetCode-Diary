""" HJ52 - 计算字符串的距离

题目：https://www.nowcoder.com/practice/3959837097c7413a961a135d7104c314
题解（动态规划）：https://blog.nowcoder.net/n/7e660f822b124e3d9a2f35e79b454099
"""
try:
    while True:
        str1, str2 = input().strip(), input().strip()
        m, n = len(str1), len(str2)

        # 动态规划矩阵
        dp = [[1 for _ in range(n + 1)] for _ in range(m + 1)]
        for _ in range(n + 1):
            dp[0][_] = _
        for _ in range(m + 1):
            dp[_][0] = _

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    # 两个字符相同，其距离不变
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 字符串修改有替换、插入、删除，选择其中改动最小的方式
                    temp = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
                    dp[i][j] = temp + 1
        print(dp[m][n])
except Exception:
    pass
