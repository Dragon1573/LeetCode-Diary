#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#
from typing import List


# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p, q = 0, len(s) - 1
        while p < q:
            s[p], s[q] = s[q], s[p]
            p, q = p + 1, q - 1
# @lc code=end
