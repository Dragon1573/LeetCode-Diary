#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (38.32%)
# Likes:    6675
# Dislikes: 0
# Total Accepted:    1.4M
# Total Submissions: 3.7M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
#
#
#
# 示例 1:
#
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
# 示例 2:
#
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
# 示例 3:
#
#
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#
# 示例 4:
#
#
# 输入: s = ""
# 输出: 0
#
#
#
#
# 提示：
#
#
# 0
# s 由英文字母、数字、符号和空格组成
#
#
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 初始化两个索引指针
        p = q = longest = 0
        length = len(s)
        if length <= 1:
            # 字符串长度在2个字符以下，不可能出现重复
            return length
        else:
            # 不断向后滑动扫描
            while q < length:
                q += 1
                if q - p > longest:
                    # 更新字串长度
                    longest = q - p
                if q == length:
                    # 右指针索引溢出，结束扫描
                    break
                elif s[q] in s[p:q]:
                    # 左指针移动到重复字符的下一个字符位
                    p += s[p:q].index(s[q]) + 1
        return longest
# @lc code=end
