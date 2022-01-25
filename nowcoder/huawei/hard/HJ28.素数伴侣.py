""" HJ28 - 素数伴侣

# 描述

若两个正整数的和为素数，则这两个正整数称之为『素数伴侣』，如 2 和 5 、 6 和 13 ，它们能应用于通信加密。

现在密码学会请你设计一个程序，从已有的 N（N 为偶数）个正整数中挑选出若干对组成『素数伴侣』。

挑选方案多种多样，例如有4个正整数：2, 5, 6, 13，如果将 5 和 6 分为一组中只能得到一组『素数伴侣』，
而将 2 和 5 、6 和 13 编组将得到两组『素数伴侣』，能组成『素数伴侣』最多的方案称为『最佳方案』，
当然密码学会希望你寻找出『最佳方案』。

本题有多组输入。

# 数据范围

1 <= n <= 100 ，输入的数据大小满足 2 <= val <= 30000

# 输入

有一个正偶数 n ，表示待挑选的自然数的个数。后面给出 n 个具体的数字。

# 输出

输出一个整数 K ，表示你求得的『最佳方案』组成『素数伴侣』的对数。

# 示例

输入：
    4
    2 5 6 13
    2
    3 6
输出：
    2
    0

输入：
    2
    3 6
输出：0
"""


def is_prime(s: int) -> bool:
    """ 素数判定（对数时间复杂度） """
    if 1 < s < 4:
        return True
    for i in range(2, int(s**0.5) + 1):
        if s % i == 0:
            return False
    return True


def find_even(evens, previous_select, final_select, odd):
    """ 寻找配对偶数 """
    for i, even in enumerate(evens):
        # 遍历所有的偶数
        if is_prime(even + odd) and previous_select[i] == 0:
            # 当前偶数＋给定奇数是素数，且这个偶数之前没有被选用过
            previous_select[i] = 1
            # 当前偶数没有匹配成功，或者它的匹配奇数是否有其他选择
            # 如果有其他选择，则当前的奇数匹配当前偶数
            if final_select[i] == 0 or find_even(
                    evens, previous_select, final_select, final_select[i]):
                final_select[i] = odd
                return True
    return False


while True:
    try:
        N = int(input())
        array = [int(_) for _ in input().strip().split()]
        count = 0
        # 所有的素数都是奇数，奇数＋偶数才有可能组成素数
        evens = [_ for _ in array if _ & 1 == 0]
        odds = [_ for _ in array if _ & 1 == 1]
        # 与各偶数配对的奇数
        final_select = [0] * len(evens)
        for odd in odds:
            # 遍历所有的奇数
            previous_select = [0] * len(evens)
            # 若找到了给定奇数所匹配的偶数，则累计匹配组数
            if find_even(evens, previous_select, final_select, odd):
                count += 1
        print(count)
    except Exception:
        break
