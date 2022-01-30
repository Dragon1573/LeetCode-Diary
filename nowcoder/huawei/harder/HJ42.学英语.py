""" HJ42 - 学英语

# 描述

编写程序将数字转换成英文。

1. 在英语读法中三位数字看成一整体，后面再加一个计数单位。从最右边往左数，三位一单位，例如 12,345 等；
2. 每三位数后记得带上计数单位，分别是 thousand 和 million ；
3. 百万以下千以上的数 X thousand X ，10亿以下百万以上的数：X million X thousand X ；
4. 在英式英语中百位数和十位数之间要加 and ；百分位为零的话，我们省略 and ；

说明：
1. 数字为正整数，不考虑小数，转化结果为英文小写；
2. 保证输入的合法性
3. 关键字提示：and, million, thousand, hundred

数据范围： 1 <= n <= 2000000

本体含有多组输入！

# 输入描述

输入多行 long 型整数

# 输出描述

输出相应的英文写法

# 示例

输入：
    22
    100
    145
    1234
    8088
    486669
    1652510
输出：
    twenty two
    one hundred
    one hundred and forty five
    one thousand two hundred and thirty four
    eight thousand eighty eight
    four hundred and eighty six thousand six hundred and sixty nine
    one million six hundred and fifty two thousand five hundred and ten
"""
from sys import stdin

# 用于百位和个位
unit_map = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}
# 用于十位
ten_map = {
    '2': 'twen',
    '3': 'thir',
    '4': 'for',
    '5': 'fif',
    '6': 'six',
    '7': 'seven',
    '8': 'eigh',
    '9': 'nine'
}


def num2repr(n: str) -> str:
    """ 将三位数转换为英语表示 """
    result = []
    if n[0] > '0':
        # 百位大于0是有效位
        result.append(unit_map[n[0]] + ' hundred')
        if n[1:] != '00':
            # 检查是否为整百，此时不需要加 and
            result.append('and')
    if n[1] == '1':
        # 检查十位是否为 1 ，10～12 有点特殊
        if n[2] == '0':
            result.append('ten')
        elif n[2] == '1':
            result.append('eleven')
        elif n[2] == '2':
            result.append('twelve')
        else:
            # 13～19 加后缀 teen
            result.append(ten_map[n[2]] + 'teen')
    elif n[1] >= '2':
        # 十位 2～9 加后缀 ty
        result.append(ten_map[n[1]] + 'ty')
    if n[1] != '1' and n[2] > '0':
        # 不是 10～19 的范围，才会单独表示个位
        result.append(unit_map[n[2]])
    # 输出拼接结果
    return ' '.join(result)


for line in stdin:
    # 将数值右对齐填充到9位数，方便分组计算
    n = line.strip().zfill(9)
    # 按千分位符进行分段
    array = [n[_:_ + 3] for _ in range(0, 9, 3)]
    # 每一段独立转换为英语表示
    array = [num2repr(_) for _ in array]
    # 补充百万位和千位中缀
    result = []
    if array[0]:
        result.append(array[0] + ' million')
    if array[1]:
        result.append(array[1] + ' thousand')
    if array[2]:
        result.append(array[2])
    # 返回拼接结果
    print(' '.join(result))
