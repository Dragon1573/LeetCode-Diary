""" HJ40 - 统计字符

https://www.nowcoder.com/practice/539054b4c33b4776bc350155f7abd8f5
"""
from sys import stdin

for line in stdin:
    counter = [0] * 4
    for _ in line.strip():
        if _.isdigit():
            counter[2] += 1
        elif _.isalpha():
            counter[0] += 1
        elif _ == ' ':
            counter[1] += 1
        else:
            counter[3] += 1
    print(*counter, sep='\n')
