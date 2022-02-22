""" HJ71 - 字符串通配符

http://www.nowcoder.com/practice/43072d50a6eb44d2a6c816a283b02036
https://blog.nowcoder.net/n/3cba504f7fd949ffb319bf7f6002d478
"""


class Solution(object):
    def match(self, p: str, s: str) -> bool:
        # 边界条件
        if not s and not p:
            return True
        elif s and not p:
            return False
        elif not s:
            return not p.replace('*', '')
        else:
            n, m = len(s), len(p)
            if (p[m - 1] == '?' and s[n - 1].isalnum()
                ) or p[m - 1].lower() == s[n - 1].lower():
                # 通配符是问号或字符
                return self.match(p[:m - 1], s[:n - 1])
            elif p[m - 1] == '*':
                return self.match(p[:m - 1], s) or self.match(p, s[:n - 1])
            else:
                return False


try:
    so = Solution()
    while True:
        p, s = input(), input()
        print(str(so.match(p, s)).lower())
except Exception:
    pass
