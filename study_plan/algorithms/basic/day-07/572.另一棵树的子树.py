#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
#
# https://leetcode-cn.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (47.44%)
# Likes:    629
# Dislikes: 0
# Total Accepted:    97.6K
# Total Submissions: 205.8K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
#
#
# 给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true
# ；否则，返回 false 。
#
# 二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。
#
#
#
# 示例 1：
#
#
# 输入：root = [3,4,5,1,2], subRoot = [4,1,2]
# 输出：true
#
#
# 示例 2：
#
#
# 输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# 输出：false
#
#
#
#
# 提示：
#
#
# root 树上的节点数量范围是 [1, 2000]
# subRoot 树上的节点数量范围是 [1, 1000]
# -10^4 <= root.val <= 10^4
# -10^4 <= subRoot.val <= 10^4
#
#
#
#
#
from typing import Union


class TreeNode:
    def __init__(self, val=0, _left=None, _right=None):
        self.val = val
        self.left = _left
        self.right = _right

    def __repr__(self):
        return 'TreeNode(v={}, left={}, right={})'.format(
            self.val, self.left, self.right)


# @lc code=start
class Solution:
    def compare(self, node: TreeNode, subRoot: TreeNode) -> bool:
        if node.val != subRoot.val:
            # 不匹配
            return False
        left, right = True, True
        if node.left and subRoot.left:
            # 两者左树都存在，递归比较
            left = self.compare(node.left, subRoot.left)
        elif node.left or subRoot.left:
            # 仅有其一存在，必然不匹配
            return False
        if node.right and subRoot.right:
            # 两者右树都存在，递归比较
            right = self.compare(node.right, subRoot.right)
        elif node.right or subRoot.right:
            return False
        # 两者的左树与右树必须同时相同
        return left and right

    def findSubRoot(self, node: TreeNode, value: int) -> Union[TreeNode, None]:
        if node.val == value:
            # 直接命中
            return node
        left, right = None, None
        if node.left:
            # 递归地搜索左树
            left = self.findSubRoot(node.left, value)
        if node.right:
            # 递归地搜索右树
            right = self.findSubRoot(node.right, value)
        # 返回其中不为空的子树
        return left if left else right

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not (root and subRoot):
            # 任何一侧是空树都不可能返回 True
            return False
        # 递归地在主树中寻找子树的根节点
        targetRoot = self.findSubRoot(root, subRoot.val)
        result = False
        while targetRoot and not result:
            # 如果它们已经出现匹配的子树了，无需递归判断
            result = result or self.compare(targetRoot, subRoot)
            # 将已经判断过的子树根节点移开
            targetRoot.val = subRoot.val + 1
            targetRoot = self.findSubRoot(root, subRoot.val)
        return result


# @lc code=end
