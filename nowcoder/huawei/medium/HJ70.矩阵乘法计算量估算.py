""" HJ70 - 矩阵乘法计算量估算

https://www.nowcoder.com/practice/15e41630514445719a942e004edc0a5b
"""
try:
    while True:
        # 数据输入
        n = int(input())
        array = [[int(x) for x in input().split()] for _ in range(n)]
        formula = input().strip()

        order, result = [], 0
        for _ in formula:
            # 遍历计算公式
            if _.isalpha():
                # 字母部分加入计算顺序表中
                order.append(array[ord(_) - ord('A')])
            elif _ == ')' and len(order) >= 2:
                # 题目限制输入合法，每组括号内将只有2个矩阵相乘
                a = order.pop()
                b = order.pop()
                # 矩阵 [a, b] × [b, c] 的结果大小为 [a, c] ，每一项需要计算 b 次乘法
                result += b[0] * b[1] * a[1]
                order.append([b[0], a[1]])
        print(result)
except Exception:
    pass
