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
if __name__ == '__main__':
    string = input()
    string = string.replace('{', '(')
    string = string.replace('[', '(')
    string = string.replace('}', ')')
    string = string.replace(']', ')')
    print(int(eval(string)))
