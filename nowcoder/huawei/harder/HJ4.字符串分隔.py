""" HJ4 - 字符串分隔

# 描述

- 连续输入字符串，请按长度为 8 拆分每个输入字符串并进行输出；
- 长度不是 8 整数倍的字符串请在后面补数字 0 ，空字符串不处理。

（注：本题有多组输入）

# 示例

输入：
    abc
    123456789
输出：
    abc00000
    12345678
    90000000
"""
from sys import stdin

for line in stdin:
    string = line.strip()
    for _ in range(0, len(string), 8):
        print(string[_:_ + 8].ljust(8, '0'))
