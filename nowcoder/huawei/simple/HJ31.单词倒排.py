"""
# HJ31 - 单词倒排

时间限制：C/C++ 1秒，其他 2秒
空间限制：C/C++ 32MB ，其他 64MB

## 描述

对字符串中的所有单词进行倒排。

说明：

1. 构成单词的字符只有 26 个大写或小写英文字母；
2. 非构成单词的字符均视为单词间隔符；
3. 要求倒排后的单词间隔符以一个空格表示；如果原字符串中相邻单词间有多个间隔符时，倒排转换后也只允许出现一个空格间隔符；
4. 每个单词最长 20 个字母；

数据范围：字符串长度满足 1 <= n <= 10000

## 示例

输入：I am a student
输出：student a am I

输入：$bo*y gi!r#l
输出：l r gi y bo
"""
from re import findall

if __name__ == '__main__':
    string = input()
    result = findall(r'[A-Za-z]+', string)
    print(' '.join(result[::-1]))
