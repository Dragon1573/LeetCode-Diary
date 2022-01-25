""" HJ106 - 字符逆序

# 描述

将一个字符串 s 的内容颠倒过来，并输出。

数据范围：1 <= len(s) <= 10000

# 输入描述

输入一个字符串，可以有空格

# 示例

输入：I am a student
输出：tneduts a ma I

输入：nowcoder
输出：redocwon
"""
from sys import stdin

for line in stdin:
    # 内置反向切片
    print(line.strip()[::-1])
