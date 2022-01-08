#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (76.88%)
# Likes:    819
# Dislikes: 0
# Total Accepted:    260K
# Total Submissions: 338.2K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
#
# 你可以按 任何顺序 返回答案。
#
#
#
# 示例 1：
#
#
# 输入：n = 4, k = 2
# 输出：
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
#
# 示例 2：
#
#
# 输入：n = 1, k = 1
# 输出：[[1]]
#
#
#
# 提示：
#
#
# 1
# 1
#
#
#
from typing import List


# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def merge(array: List[int], k: int) -> List[List[int]]:
            if k == 1:
                # 当只从列表中选一项时，只输出各元素自身组成的列表
                return [[i] for i in array]
            else:
                result = []
                for i in range(len(array) - k + 1):
                    last = merge(array[i + 1:], k - 1)
                    for j in last:
                        result.append([array[i]] + j)
                return result

        return merge(list(range(1, n + 1)), k)


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.combine(20, 10))
