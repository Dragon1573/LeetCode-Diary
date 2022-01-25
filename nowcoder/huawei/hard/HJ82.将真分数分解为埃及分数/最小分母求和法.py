""" HJ82 - 将真分数分解为埃及分数

# 最小分母求和法

我们认为，n/d = sum(1/a + 1/b + 1/c + ... + 1/d) ，其中 a < b < c < ... < d 。

# 示例

1/2+1/5+1/37+1/4070 = 8/11
1/2 = 2/4
"""
from sys import stdin

for line in stdin:
    n, d = map(int, line.strip().split('/'))
    target = n / d
    i, result = 2, []
    while abs(target) > 1e-6:
        if target - 1 / i >= 0:
            result.append('1/' + str(i))
            target -= 1 / i
        i += 1
    print('+'.join(result))
