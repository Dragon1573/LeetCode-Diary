""" HJ9 - 提取不重复的整数

https://www.nowcoder.com/practice/253986e66d114d378ae8de2e6c4577c1
"""
if __name__ == '__main__':
    n = int(input())
    array = []
    while n:
        x = n % 10
        if x not in array:
            array.append(x)
        n //= 10
    print(*array, sep='')
