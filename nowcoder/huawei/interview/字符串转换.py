""" 实现一个 atoi 函数

# 描述

1. 空白字符前缀不影响结果；
2. 负号前缀表示有符号负值；
3. 非数值前缀无法完成转换；
4. 非数值后缀不影响结果；
5. 结果为32位有符号整数，有效数值范围 [-(2**31), (2**31 - 1)]。

非法结果统一输出 0 ，数值越界时分别输出上下界值。
"""
from unittest import TestCase, main


class String2Int(TestCase):
    INT_MIN, INT_MAX = -(2**31), (2**31 - 1)

    def atoi(self, string: str) -> int:
        result, flag = 0, 1
        for _ in string:
            if _ == ' ':
                continue
            elif _ == '-':
                flag = -1
            elif _.isdigit():
                result *= 10
                result += ord(_) - ord('0')
            else:
                break
        if flag * result < self.INT_MIN:
            return self.INT_MIN
        elif flag * result > self.INT_MAX:
            return self.INT_MAX
        else:
            return flag * result

    def test_01(self):
        self.assertEqual(42, self.atoi('42'))

    def test_02(self):
        self.assertEqual(-42, self.atoi(' -42'))

    def test_03(self):
        self.assertEqual(1234, self.atoi('1234 with words'))

    def test_04(self):
        self.assertEqual(0, self.atoi('words and 6789'))

    def test_05(self):
        self.assertEqual(self.INT_MIN, self.atoi('-98765432109876543210'))


if __name__ == "__main__":
    main()
