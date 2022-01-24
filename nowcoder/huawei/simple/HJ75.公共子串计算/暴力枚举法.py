""" HJ75 - 公共子串计算（暴力枚举法） """
if __name__ == "__main__":
    a, b = input(), input()
    if len(a) > len(b):
        a, b = b, a
    result = 0

    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[i:j + 1] in b and j + 1 - i > result:
                result = j + 1 - i

    print(result)
