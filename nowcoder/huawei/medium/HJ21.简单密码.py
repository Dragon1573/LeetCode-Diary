""" HJ21 - 简单密码

https://www.nowcoder.com/practice/7960b5038a2142a18e27e4c733855dac
"""
from sys import stdin


def convert(s: str) -> str:
    if s.islower():
        # 小写字母映射为数字
        if s in 'abc':
            return '2'
        elif s in 'def':
            return '3'
        elif s in 'ghi':
            return '4'
        elif s in 'jkl':
            return '5'
        elif s in 'mno':
            return '6'
        elif s in 'pqrs':
            return '7'
        elif s in 'tuv':
            return '8'
        else:
            return '9'
    elif s.isupper():
        # 大写字母映射为小写字母
        return chr((ord(s) - 64) % 26 + 97)
    else:
        # 其他字符不变
        return s


for line in stdin:
    print(''.join(map(convert, line.strip())))
