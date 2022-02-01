""" HJ16 - 购物单（0-1背包问题）

https://www.nowcoder.com/practice/f9c6f980eeec43ef85be20755ddbeaf4
https://blog.nowcoder.net/n/82b5f014a8654c8b8dbff4fe4fa727bd
"""
if __name__ == '__main__':
    # 成本与物品数量
    n, m = map(int, input().split())
    # 主件与配件
    primary, annex = {}, {}
    for i in range(1, m + 1):
        # 循环获取输入
        v, p, q = map(int, input().split())
        if q == 0:
            primary[i] = [v, p]
        else:
            if q in annex:
                annex[q].append([v, p])
            else:
                annex[q] = [[v, p]]

    # 动态规划
    dp = [0] * (n + 1)
    for key in primary:
        # 价格与得分
        v_mat, p_mat = [], []

        # 主件
        v_mat.append(primary[key][0])
        p_mat.append(primary[key][0] * primary[key][1])
        if key in annex:
            # 存在附件

            # 主件＋附件A
            v_mat.append(v_mat[0] + annex[key][0][0])
            p_mat.append(p_mat[0] + annex[key][0][0] * annex[key][0][1])
            if len(annex[key]) > 1:
                # 主件拥有两个附件

                # 主件＋附件B
                v_mat.append(v_mat[0] + annex[key][1][0])
                p_mat.append(p_mat[0] + annex[key][1][0] * annex[key][1][1])

                # 主件＋两个附件
                v_mat.append(v_mat[0] + annex[key][0][0] + annex[key][1][0])
                p_mat.append(p_mat[0] + annex[key][0][0] * annex[key][0][1] +
                             annex[key][1][0] * annex[key][1][1])

        for j in range(n, -1, -10):
            # 物品价格都是 10 的倍数
            for k in range(len(v_mat)):
                if j - v_mat[k] >= 0:
                    dp[j] = max(dp[j], dp[j - v_mat[k]] + p_mat[k])
    print(dp[n])
