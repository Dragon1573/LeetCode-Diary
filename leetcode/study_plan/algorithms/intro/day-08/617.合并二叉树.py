#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#
# https://leetcode-cn.com/problems/merge-two-binary-trees/description/
#
# algorithms
# Easy (78.68%)
# Likes:    843
# Dislikes: 0
# Total Accepted:    215.5K
# Total Submissions: 273.9K
# Testcase Example:  '[1,3,2,5]\n[2,1,3,null,4,null,7]'
#
# 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
#
# 你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL
# 的节点将直接作为新二叉树的节点。
#
# 示例 1:
#
#
# 输入:
# Tree 1                     Tree 2
# ⁠         1                         2
# ⁠        / \                       / \
# ⁠       3   2                     1   3
# ⁠      /                           \   \
# ⁠     5                             4   7
# 输出:
# 合并后的树:
#     3
#    / \
#   4   5
#  / \   \
# 5   4   7
#
#
# 注意: 合并必须从两个树的根节点开始。
#
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def singleMerge(node01: TreeNode, node02: TreeNode) -> TreeNode:
            if node01 is None:
                return node02
            elif node02 is None:
                return node01
            else:
                return TreeNode(node01.val + node02.val,
                                singleMerge(node01.left, node02.left),
                                singleMerge(node01.right, node02.right))

        return singleMerge(root1, root2)


# @lc code=end
