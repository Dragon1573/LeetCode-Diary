""" HJ73 - 计算日期到天数转换

时间限制：C/C++ 1秒，其他 2秒
空间限制：C/C++ 32MB ，其他 64MB

## 描述

根据输入的日期，计算是这一年的第几天。保证年份为4位数且日期合法。

## 进阶
时间复杂度：O(n)
空间复杂度：O(1)

## 输入描述

输入一行，每行空格分割，分别是年、月、日

## 输出描述

输出是这一年的第几天

## 示例

输入：2012 12 31
输出：366

输入：1982 3 4
输出：63
"""
from datetime import date

if __name__ == '__main__':
    year, month, day = map(int, input().strip().split())
    target = date(year, month, day)
    start = date(year, 1, 1)
    print((target - start).days + 1)
