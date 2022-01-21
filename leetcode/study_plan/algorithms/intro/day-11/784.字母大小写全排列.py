#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#
# https://leetcode-cn.com/problems/letter-case-permutation/description/
#
# algorithms
# Medium (69.05%)
# Likes:    340
# Dislikes: 0
# Total Accepted:    51K
# Total Submissions: 73.8K
# Testcase Example:  '"a1b2"'
#
# 给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
#
#
#
# 示例：
# 输入：S = "a1b2"
# 输出：["a1b2", "a1B2", "A1b2", "A1B2"]
#
# 输入：S = "3z4"
# 输出：["3z4", "3Z4"]
#
# 输入：S = "12345"
# 输出：["12345"]
#
#
#
#
# 提示：
#
#
# S 的长度不超过12。
# S 仅由数字和字母组成。
#
#
#
from typing import List


# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        s, results = s.lower(), []

        def search(prefix: str, suffix: str) -> None:
            if not suffix:
                results.append(prefix)
            else:
                search(prefix + suffix[0], suffix[1:])
                if suffix[0].isalpha():
                    search(prefix + suffix[0].upper(), suffix[1:])

        search("", s)
        return results


# @lc code=end
if __name__ == "__main__":
    print(Solution().letterCasePermutation("12345"))
