""" HJ23 - 删除字符串中出现次数最少的字符

# 描述

实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。
输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
注意每个输入文件有多组输入，即多个字符串用回车隔开。

数据范围：输入的字符串长度满足 1 <= n <= 20 ，保证输入的字符串中仅出现小写字母。

# 输入描述

字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。

# 输出描述

删除字符串中出现次数最少的字符后的字符串。

# 示例

输入：
    abcdd
    aabcddd
输出：
    abcdd
    aabcddd
"""
from collections import Counter
from sys import stdin

for line in stdin:
    # 统计字符词频，生成 字符-频数 键值对数组
    counter = [(k, v) for k, v in Counter(line.strip()).items()]
    # 按频数降序排序
    counter.sort(key=lambda _: _[1], reverse=True)
    # 获取最少的频数
    count = counter[-1][1]
    # 构造字符列表
    array = [_ for _ in line.strip()]
    while counter[-1][1] == count:
        # 列表过滤，移除相应的字符
        array = [_ for _ in array if _ != counter[-1][0]]
        counter.pop()
    print(*array, sep='')
