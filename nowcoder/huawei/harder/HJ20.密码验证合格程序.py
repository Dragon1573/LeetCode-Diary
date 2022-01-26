""" HJ20 - 密码验证合格程序

# 描述

密码要求:

1. 长度超过8位
2. 包括大小写字母、数字、其它符号，以上四种至少三种
3. 不能有长度大于2的不含公共元素的子串重复（注：其他符号不含空格或换行）

数据范围：输入的字符串长度满足 1 <= n <= 100

本题有多组输入。

# 输入描述

一组或多组字符串。每组占一行

# 输出描述

如果符合要求输出 OK ，否则输出 NG

# 示例

输入：
    021Abc9000
    021Abc9Abc1
    021ABC9000
    021$bc9000
输出：
    OK
    NG
    NG
    OK
"""
from sys import stdin


def check_type(s: str) -> bool:
    """ 字符类型数量检查 """
    counter = [False] * 4
    for _ in s:
        if _.isupper():
            counter[0] = True
        elif _.islower():
            counter[1] = True
        elif _.isdigit():
            counter[2] = True
        else:
            counter[3] = True
    return sum(counter) >= 3


def check_repeat(s: str) -> bool:
    # 枚举所有可能的子串片段
    for i in range(len(s)):
        for j in range(i, min(len(s), 2 * i)):
            # 检查子串长度，判断是否在前面的子串中重复
            if j - i > 2 and s[i:j] in s[:i]:
                return False
    return True


for line in stdin:
    line = line.strip()
    # 要求一
    is_valid = True and (len(line) > 8)
    # 要求二
    is_valid = is_valid and check_type(line)
    # 要求三
    is_valid = is_valid and check_repeat(line)
    print('OK' if is_valid else 'NG')
