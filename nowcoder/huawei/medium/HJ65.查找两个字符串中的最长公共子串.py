""" HJ65 - 查找两个字符串a,b中的长公共子串

https://www.nowcoder.com/practice/181a1a71c7574266ad07f9739f791506
"""
le True:
        a = input().strip()
        b = input().strip()
        if len(a) > len(b):
            a, b = b, a
        
        match_length, bounds = 0, (0, 0)
        size_a = len(a)
        for i in range(size_a):
            for j in range(i + 1, size_a + 1):
                if a[i:j] in b and (j - i) > match_length:
                    match_length = j - i
                    bounds = (i, j)

        print(a[bounds[0]:bounds[1]])
except Exception:
    pass
