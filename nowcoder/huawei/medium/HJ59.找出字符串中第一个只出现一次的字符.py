""" HJ59 - 找出字符串中第一个只出现一次的字符

https://www.nowcoder.com/practice/e896d0f82f1246a3aa7b232ce38029d4
"""
from collections import Counter
from sys import stdin

for line in stdin:
    counter = Counter(line.strip())
    counter = sorted(counter.items(), key=lambda _: _[1])
    flag = False
    for k, v in counter:
        if v == 1:
            print(k)
            flag = True
            break
    if not flag:
        print(-1)
