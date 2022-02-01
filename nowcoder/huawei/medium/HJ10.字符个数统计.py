""" HJ10 - 字符个数统计

https://www.nowcoder.com/practice/eb94f6a5b2ba49c6ac72d40b5ce95f50
"""
if __name__ == '__main__':
    string = input().strip()
    bloom = [False] * 128
    for _ in string:
        bloom[ord(_)] = True
    print(sum(bloom))
