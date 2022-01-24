""" HJ85 - 最长回文子串（暴力枚举法）

时间复杂度：O(n^2)
空间复杂度：O(1)
"""
if __name__ == '__main__':
    result = 0
    string = ' ' + input() + ' '
    for start in range(1, len(string) - 1):
        for end in range(start, len(string)):
            if string[start:end + 1] == string[end:start - 1:-1]:
                result = max(result, end - start + 1)
    print(result)
