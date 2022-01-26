""" HJ17 - 坐标移动

# 描述

开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。
从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。

输入：合法坐标为 W/A/S/D + 数字（两位以内），坐标之间以 ; 分隔。

非法坐标点需要进行丢弃。如 AA10; A1A; $%$; YAD; 等。

数据范围：
    每组输入的字符串长度满足 1 <= n <= 10000
    坐标保证满足 −2**31 <= x, y <= 2**31 −1 ，且数字部分仅含正数

注意请处理多组输入输出！

# 输入描述

一行字符串

# 输出描述

最终坐标，以逗号分隔

# 示例

输入：A10;S20;W10;D30;X;A1A;B10A11;;A10;
输出：10,-10
说明：

输入：ABC;AKL;DA1;
输出：0,0

起点（0,0）
+ A10    = (-10,0)
+ S20    = (-10,-20)
+ W10    = (-10,-10)
+ D30    = (20,-10)
+ X      = 无效
+ A1A    = 无效
+ B10A11 = 无效
+ ""     = 无影响
+ A10    = (10,-10)
结果 (10,-10)
"""
from re import match
from sys import stdin

PATTERN = r'^[WASD]\d{1,2}$'

for line in stdin:
    x, y = 0, 0
    steps = line.strip().split(';')
    for s in steps:
        if match(PATTERN, s):
            # 用正则表达式进行规则检查
            direction, distance = s[0], int(s[1:])
            if direction == 'W':
                y += distance
            elif direction == 'A':
                x -= distance
            elif direction == 'S':
                y -= distance
            elif direction == 'D':
                x += distance
    print(x, y, sep=',')
