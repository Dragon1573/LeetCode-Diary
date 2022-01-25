""" HJ27 - 查找兄弟单词

# 描述

定义一个单词的『兄弟单词』为：

    交换该单词字母顺序（注：可以交换任意次），而不添加、删除、修改原有的字母就能生成的单词。

兄弟单词要求和原来的单词不同。例如：

    ab 和 ba 是兄弟单词。
    ab 和 ab 则不是兄弟单词。

现在给定你 n 个单词，另外再给你一个单词 str ，让你寻找 str 的兄弟单词里，按字典序排列后的第 k 个单词是什么？
注意：字典中可能有重复单词。本题含有多组输入数据。

数据范围：1<= n<= 1000 ，输入的字符串长度满足 1 <= len(str)<= 10, 1 <= k < n

# 输入描述

先输入单词的个数 n ，再输入 n 个单词。 再输入一个单词，为待查找的单词 x 最后输入数字 k 。

# 输出描述

输出查找到 x 的兄弟单词的个数 m 然后输出查找到的按照字典顺序排序后的第 k 个兄弟单词，没有符合第 k 个的话则不用输出。

# 示例

输入：3 abc bca cab abc 1
输出：
    2
    bca

输入：6 cab ad abcd cba abc bca abc 1
输出：
    3
    bca
说明：
    abc 的兄弟单词有 cab cba bca ，所以输出 3
    经字典序排列后，变为 bca cab cba ，所以第 1 个字典序兄弟单词为 bca
"""
from sys import stdin
from itertools import permutations

for line in stdin:
    # 读取输入并解包
    _, *array, s, k = line.strip().split()
    # 产生给定单词的全排列，并执行去重
    nPr = set([''.join(_) for _ in permutations(list(s))])
    # 获取全排列与词典的交集，并去除输入单词自身
    array = [_ for _ in array if _ in nPr and _ != s]
    # 原地字典升序
    array.sort()
    # 输出结果
    print(len(array))
    if 1 <= int(k) <= len(array):
        print(array[int(k) - 1])
