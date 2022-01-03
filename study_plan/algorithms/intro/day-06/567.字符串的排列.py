#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
# https://leetcode-cn.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (43.38%)
# Likes:    524
# Dislikes: 0
# Total Accepted:    141K
# Total Submissions: 325.1K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
#
# 换句话说，s1 的排列之一是 s2 的 子串 。
#
#
#
# 示例 1：
#
#
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
#
#
# 示例 2：
#
#
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false
#
#
#
#
# 提示：
#
#
# 1 <= s1.length, s2.length <= 10^4
# s1 和 s2 仅包含小写字母
#
#
#
from collections import Counter


# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 获取短串的长度
        len_01 = len(s1)
        # 获取 s1 的字频
        counter_01 = Counter(s1)
        for _ in range(len(s2) - len_01 + 1):
            # 若 s1 的排列之一是 s2 的子串，
            # 则 s1 与 s2 对应子串具有相同的字频
            if counter_01 == Counter(s2[_:_ + len_01]):
                return True
        return False


# @lc code=end
