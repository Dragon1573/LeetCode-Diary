""" HJ6 - 质数因子

https://www.nowcoder.com/practice/196534628ca6490ebce2e336b47b3607
"""


def recurse(n: int, d: int) -> None:
    """ 递归求解 """
    # 借助传入的参数 d 压缩循环次数，
    # 也可以借此保证质因数不降序
    for _ in range(d, int(n**0.5) + 1):
        if n % _ == 0:
            print(_, end=' ')
            recurse(n // _, _)
            return
    print(n, end=' ')


if __name__ == '__main__':
    recurse(int(input()), 2)
