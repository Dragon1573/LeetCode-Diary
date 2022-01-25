""" HJ82 - 将真分数分解为埃及分数

# 最大公约数分解法

我们认为， n/d = n * (1/d) ，随后尽可能多地合并项并约分。

# 示例

1/11+1/11+1/11+1/11+1/11+1/11+1/11+1/11 = 8/11
1/2 = 2/4
"""
from sys import stdin

for line in stdin:
    n, d = map(int, line.strip().split("/"))
    result = ""
    num = n
    gcd = num
    first = True
    while True:
        if d % gcd == 0:
            if first:
                result += ("1/" + str(d // gcd))
            else:
                result += ("+1/" + str(d // gcd))

            n = n - gcd
            first = False
            gcd = n
            if n == 0:
                print(result)
                break

        else:
            gcd -= 1
            if gcd == 0:
                break
