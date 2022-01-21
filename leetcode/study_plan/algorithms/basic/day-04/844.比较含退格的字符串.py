#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#
# https://leetcode-cn.com/problems/backspace-string-compare/description/
#
# algorithms
# Easy (50.69%)
# Likes:    354
# Dislikes: 0
# Total Accepted:    105.2K
# Total Submissions: 207.6K
# Testcase Example:  '"ab#c"\n"ad#c"'
#
# 给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，请你判断二者是否相等。# 代表退格字符。
#
# 如果相等，返回 true ；否则，返回 false 。
#
# 注意：如果对空文本输入退格字符，文本继续为空。
#
#
#
# 示例 1：
#
#
# 输入：s = "ab#c", t = "ad#c"
# 输出：true
# 解释：S 和 T 都会变成 “ac”。
#
#
# 示例 2：
#
#
# 输入：s = "ab##", t = "c#d#"
# 输出：true
# 解释：s 和 t 都会变成 “”。
#
#
# 示例 3：
#
#
# 输入：s = "a##c", t = "#a#c"
# 输出：true
# 解释：s 和 t 都会变成 “c”。
#
#
# 示例 4：
#
#
# 输入：s = "a#c", t = "b"
# 输出：false
# 解释：s 会变成 “c”，但 t 仍然是 “b”。
#
#
#
# 提示：
#
#
# 1 <= s.length, t.length <= 200
# s 和 t 只含有小写字母以及字符 '#'
#
#
#
#
# 进阶：
#
#
# 你可以用 O(N) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？
#
#
#
#
#


# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """ 字符是否被删除只与后一个字符有关，逆序遍历确认是否需要删除字符 """
        p, q = len(s) - 1, len(t) - 1
        # 记录删除的字符个数
        skipS = skipT = 0

        while p >= 0 or q >= 0:
            # 持续遍历到两个字符串结束
            while p >= 0:
                # 持续遍历到首字符串结束
                if s[p] == '#':
                    # 遇到退格字符
                    skipS += 1
                    p -= 1
                elif skipS > 0:
                    # 移除字符
                    skipS -= 1
                    p -= 1
                else:
                    # 有效字符
                    break
            while q >= 0:
                if t[q] == '#':
                    skipT += 1
                    q -= 1
                elif skipT > 0:
                    skipT -= 1
                    q -= 1
                else:
                    break
            if p >= 0 and q >= 0:
                if s[p] != t[q]:
                    # 两个字符串中间对应位置的字符不匹配
                    return False
            elif p >= 0 or q >= 0:
                # 两个字符串不等长
                return False
            # 继续比较前一位字符
            p, q = p - 1, q - 1
        # 否则是相同的
        return True


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    assert s.backspaceCompare("ab#c", "ad#c") is True
    assert s.backspaceCompare("ab##", "c#d#") is True
    assert s.backspaceCompare("a##c", "#a#c") is True
    assert s.backspaceCompare("a#c", "b") is False
    assert s.backspaceCompare("y#fo##f", "y#f#o##f") is True
