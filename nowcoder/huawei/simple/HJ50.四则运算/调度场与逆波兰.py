"""
# HJ50 - 四则运算

时间限制：C/C++ 1秒，其他 2秒
空间限制：C/C++ 32MB ，其他 64MB

## 描述

输入一个表达式（用字符串表示），求这个表达式的值。

保证字符串中的有效字符包括 ['0'-'9'], '+', '-', '*', '/' , '('， ')', '[', ']', '{' , '}'。
且表达式一定合法。

数据范围：表达式计算结果和过程中满足 |val| <= 1000 ，字符串长度满足 1 <= n <= 1000
"""
from typing import List

MP = '+-*/)]}'


def compare(x: str, y: str) -> bool:
    if x == '(':
        return False
    elif x in ['+', '-'] and y in ['*', '/']:
        return False
    return True


def calculate(nums: List[int], ops: List[str]) -> None:
    b = nums.pop()
    a = nums.pop()
    op = ops.pop()
    if op == '+':
        a += b
    elif op == '-':
        a -= b
    elif op == '*':
        a *= b
    elif op == '/':
        a //= b
    nums.append(a)


if __name__ == '__main__':
    string = input()
    n, o = [], []
    o.append('(')
    string += ')'
    isNextOp = False
    _ = 0
    while _ < len(string):
        if string[_] in ['(', '[', '{']:
            o.append('(')
        elif string[_] in [')', ']', '}']:
            while o[-1] != '(':
                calculate(n, o)
            o.pop()
        elif isNextOp:
            while compare(o[-1], string[_]):
                calculate(n, o)
            o.append(string[_])
            isNextOp = False
        else:
            j = _
            if string[j] in ['+', '-']:
                _ += 1
            while MP.find(string[_]) == -1:
                _ += 1
            t = string[j:_]
            n.append(int(t))
            _ -= 1
            isNextOp = True
        _ += 1
    print(n[-1])
