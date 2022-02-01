""" HJ45 - 名字的漂亮度

https://www.nowcoder.com/practice/02cb8d3597cf416d9f6ae1b9ddc4fde3
"""
from collections import Counter

try:
    while True:
        n = int(input())
        for _ in range(n):
            counter = Counter(input().strip())
            counter = sorted(counter.items(), key=lambda _: _[1], reverse=True)
            print(sum(i * v for i, (_, v) in zip(range(26, 0, -1), counter)))
except Exception:
    pass
