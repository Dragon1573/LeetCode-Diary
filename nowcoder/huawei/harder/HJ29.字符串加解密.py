""" HJ29 - 字符串加解密

# 描述

1. 对输入的字符串进行加解密，并输出。
2. 加密方法为：
    当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写，
    如字母 a 时则替换为 B ；字母 Z 时则替换为 a ；
    当内容是数字时则把该数字加 1 ，如 0 替换 1 ， 1 替换 2 ， 9 替换 0 ；
    其他字符不做变化。
3. 解密方法为加密的逆过程。

本题含有多组样例输入。

数据范围：输入的两个字符串长度满足 1 <= n <= 1000 ，保证输入的字符串都是大小写字母或者数字。

# 输入说明

输入一串要加密的密码，再输入一串加过密的密码

# 输出描述

输出加密后的字符，再输出解密后的字符

# 示例

输入：
    abcdefg
    BCDEFGH
输出：
    BCDEFGH
    abcdefg
"""
from sys import stdin

# 标记当前运算方向
encode = True
# 字符交换表
SWITCH_TABLE = ['aBcDeFgHiJkLmNoPqRsTuVwXyZ', 'AbCdEfGhIjKlMnOpQrStUvWxYz']


def encrypter(raw: str) -> str:
    """ 加密函数 """
    if raw.islower():
        # 小写字符
        if ord(raw) & 1:
            # ord('a') = 97 ，这些小写字符在第一个表中
            index = SWITCH_TABLE[0].index(raw)
            # 加密是后移一位
            return SWITCH_TABLE[0][(index + 1) % 26]
        else:
            # ord('b') = 98 ，这些小写字符在第二个表中
            index = SWITCH_TABLE[1].index(raw)
            return SWITCH_TABLE[1][(index + 1) % 26]
    if raw.isupper():
        # 大写字符同理
        if ord(raw) & 1:
            index = SWITCH_TABLE[1].index(raw)
            return SWITCH_TABLE[1][(index + 1) % 26]
        else:
            index = SWITCH_TABLE[0].index(raw)
            return SWITCH_TABLE[0][(index + 1) % 26]
    elif raw.isdigit():
        # ord('0') = 48 ，直接借助 ASCII 值进行计算
        return chr((ord(raw) - 47) % 10 + 48)
    else:
        # 其他字符不变
        return raw


def decrypter(raw: str) -> str:
    """ 解密函数 """
    if raw.isupper():
        if ord(raw) & 1:
            index = SWITCH_TABLE[1].index(raw)
            # 解密为前移一位
            return SWITCH_TABLE[1][(index - 1) % 26]
        else:
            index = SWITCH_TABLE[0].index(raw)
            return SWITCH_TABLE[0][(index - 1) % 26]
    if raw.islower():
        if ord(raw) & 1:
            index = SWITCH_TABLE[0].index(raw)
            return SWITCH_TABLE[0][(index - 1) % 26]
        else:
            index = SWITCH_TABLE[1].index(raw)
            return SWITCH_TABLE[1][(index - 1) % 26]
    elif raw.isdigit():
        # 当 raw = '0' 时，数值前移会产生负数
        # 因此我们少减去 10 以免产生负数值
        return chr((ord(raw) - 39) % 10 + 48)
    else:
        return raw


for line in stdin:
    if encode:
        # 加密方向
        result = list(map(encrypter, line.strip()))
    else:
        # 解密方向
        result = list(map(decrypter, line.strip()))
    print(*result, sep='')
    # 切换加解密状态
    encode = not encode
