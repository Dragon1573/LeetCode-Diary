""" HJ33 - 整数与IP地址间的转换

# 描述

原理：ip地址的每段可以看成是一个 0-255 的整数，把每段拆分成一个二进制形式组合起来，
然后把这个二进制数转变成一个长整数。
举例：一个ip地址为 10.0.3.193
每段数字        相对应的二进制数
10             00001010
0              00000000
3              00000011
193            11000001

组合起来即为：00001010 00000000 00000011 11000001，转换为10进制数就是：167773121，
即该IP地址转换后的数字就是它了。

本题含有多组输入用例，每组用例需要你将一个ip地址转换为整数、将一个整数转换为ip地址。

数据范围：保证输入的是合法的 IP 序列

# 示例

输入：
    10.0.3.193
    167969729
输出：
    167773121
    10.3.3.193
"""
from sys import stdin

direction = True


def encrypt(s: str) -> int:
    parts = map(int, s.split('.'))
    parts = map(lambda _: bin(_)[2:].zfill(8), parts)
    return int(''.join(parts), base=2)


def decrypt(v: str) -> str:
    value = bin(int(v))[2:].zfill(32)
    parts = [int(value[_:_ + 8], base=2) for _ in range(0, 32, 8)]
    return '.'.join(map(str, parts))


for line in stdin:
    if direction:
        print(encrypt(line.strip()))
    else:
        print(decrypt(line.strip()))
    direction = not direction
