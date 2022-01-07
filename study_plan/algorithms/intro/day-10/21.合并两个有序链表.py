#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (66.68%)
# Likes:    2129
# Dislikes: 0
# Total Accepted:    815.7K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
#
#
# 示例 1：
#
#
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
#
#
# 示例 2：
#
#
# 输入：l1 = [], l2 = []
# 输出：[]
#
#
# 示例 3：
#
#
# 输入：l1 = [], l2 = [0]
# 输出：[0]
#
#
#
#
# 提示：
#
#
# 两个链表的节点数目范围是 [0, 50]
# -100
# l1 和 l2 均按 非递减顺序 排列
#
#
#
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        # 两种边界条件
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            # 递归解法
            if list1.val <= list2.val:
                return ListNode(list1.val,
                                self.mergeTwoLists(list1.next, list2))
            else:
                return ListNode(list2.val,
                                self.mergeTwoLists(list1, list2.next))


# @lc code=end
