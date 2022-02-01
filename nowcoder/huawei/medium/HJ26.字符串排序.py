""" HJ26 - 字符串排序

https://www.nowcoder.com/practice/5190a1db6f4f4ddb92fd9c365c944584
"""
from sys import stdin

for line in stdin:
    alpha, other = [], []
    for i, v in enumerate(line.strip()):
        if v.isalpha():
            alpha.append(v)
        else:
            other.append([i, v])
    alpha.sort(key=lambda _: _.lower())
    for i, v in other:
        alpha.insert(i, v)
    print(''.join(alpha))
