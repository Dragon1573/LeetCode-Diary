""" HJ93 - 数组分组

# 描述

输入int型数组，询问该数组能否分成两组，使得两组中各元素加起来的和相等，并且，
所有5的倍数必须在其中一个组中，所有3的倍数在另一个组中（不包括5的倍数），
不是5的倍数也不是3的倍数能放在任意一组，可以将数组分为空数组，能满足以上条件，
输出true；不满足时输出false。

本题含有多组样例输入。

数据范围：每个数组大小 1 <= n <= 50 ，输入的数据大小 |val| <= 500

# 输入描述

# 输入描述

第一行是数据个数，第二行是输入的数据

# 输出描述

返回true或者false

# 示例

输入：
    4
    1 5 -5 1
    3
    3 5 8
输出：
    true
    false
说明：
    第一个样例：
        第一组：5 -5 1
        第二组：1
    第二个样例：由于3和5不能放在同一组，所以不存在一种分法。

输入：
    2
    8 -8
输出：true
说明：由于可以将数组分为空数组，所以输出true。
"""


def dfs(remind, left, right):
    """ 递归地枚举所有可能 """
    if not remind:
        # 没有剩余元素了，是否有效取决于两侧是否相等
        return left == right
    else:
        # 将剩余元素分成首元素和后续两个部分
        x, *y = remind
        # 每个元素只能被添加到任意一侧，添加顺序是不敏感的
        return dfs(y, left + x, right) or dfs(y, left, right + x)


try:
    while True:
        _ = input()
        # 读取所有的数值
        array = [int(_) for _ in input().split()]
        # 分别计算左侧 5 倍数与 3 倍数的求和
        left = sum(_ for _ in array if _ % 5 == 0)
        right = sum(_ for _ in array if _ % 3 == 0)
        # 获取剩下所有的数值
        remind = [_ for _ in array if (_ % 3 != 0 and _ % 5 != 0)]
        print(str(dfs(remind, left, right)).lower())
except Exception:
    pass
