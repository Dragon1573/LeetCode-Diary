""" HJ14 - 字符串排序

https://www.nowcoder.com/practice/5af18ba2eb45443aa91a11e848aa6723
"""
if __name__ == '__main__':
    n = int(input())
    array = [input().strip() for _ in range(n)]
    array.sort()
    print(*array, sep='\n')
