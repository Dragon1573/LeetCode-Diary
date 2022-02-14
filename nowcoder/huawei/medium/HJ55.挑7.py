""" HJ55 - 挑7

https://www.nowcoder.com/practice/ba241b85371c409ea01ac0aa1a8d957b
"""
from sys import stdin

for line in stdin:
    n = int(line)
    count = 0
    for _ in range(2, n + 1):
        if _ % 7 == 0:
            count += 1
        elif '7' in str(_):
            count += 1
    print(count)
