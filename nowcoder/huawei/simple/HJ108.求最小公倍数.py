"""
# HJ108 - 求最小公倍数

时间限制：C/C++ 1秒，其他 2秒
空间限制：C/C++ 32MB ，其他 64MB

## 描述

正整数 A 和正整数 B 的最小公倍数是指『能被 A 和 B 整除的最小的正整数值』。设计一个算法，求输入 A 和 B 的最小公倍数。

数据范围：1 <= a, b <= 100000

## 示例

输入：5 7
输出：35

输入：2 4
输出：4
"""


def gcd(a: int, b: int) -> int:
    return gcd(b, a % b) if b else a


if __name__ == '__main__':
    x, y = map(int, input().split(' '))
    print(x * y // gcd(x, y))
