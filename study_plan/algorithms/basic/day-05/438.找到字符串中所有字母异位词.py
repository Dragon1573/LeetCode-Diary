#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (53.73%)
# Likes:    756
# Dislikes: 0
# Total Accepted:    137.6K
# Total Submissions: 255.9K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
#
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
#
#
#
# 示例 1:
#
#
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
#
#
# 示例 2:
#
#
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
#
#
#
#
# 提示:
#
#
# 1 <= s.length, p.length <= 3 * 10^4
# s 和 p 仅包含小写字母
#
#
#
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)
        if len_s < len_p:
            # 当母串长度小于子串，不可能存在异位词
            return []
        result = []
        """ 统计两个字符串的词频 """
        count = [0] * 26
        for i in range(len_p):
            count[ord(s[i]) - 97] += 1
            count[ord(p[i]) - 97] -= 1
        # 计算两个字符串的词频差异
        differ = [_ != 0 for _ in count].count(True)
        if differ == 0:
            # 若词频差异为 0 ，则出现异位词
            result.append(0)
        """ 执行滑动窗口 """
        for i in range(len_s - len_p):
            if count[ord(s[i]) - 97] == 1:
                # 两者相应字符数量从不同变得相同
                differ -= 1
            elif count[ord(s[i]) - 97] == 0:
                # 两者相应字符数量从相同变得不同
                differ += 1
            # 移除窗口左边界字符
            count[ord(s[i]) - 97] -= 1
            """ 以同样的方法操作窗口右边界 """
            if count[ord(s[i + len_p]) - 97] == -1:
                differ -= 1
            elif count[ord(s[i + len_p]) - 97] == 0:
                differ += 1
            count[ord(s[i + len_p]) - 97] += 1
            if differ == 0:
                result.append(i + 1)
        return result


# @lc code=end
