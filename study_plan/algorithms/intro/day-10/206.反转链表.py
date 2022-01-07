#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (72.47%)
# Likes:    2185
# Dislikes: 0
# Total Accepted:    817.3K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,4,5]'
#
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
#
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]
#
#
# 示例 2：
#
#
# 输入：head = [1,2]
# 输出：[2,1]
#
#
# 示例 3：
#
#
# 输入：head = []
# 输出：[]
#
#
#
#
# 提示：
#
#
# 链表中节点的数目范围是 [0, 5000]
# -5000
#
#
#
#
# 进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
#
#
#
#
from typing import Optional


class ListNode:
    def __init__(self, val=0, next: 'Optional[ListNode]' = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        array, p = [], self
        while p:
            array.append(p.val)
            p = p.next
        return str(array)


# class Solution:
#     """ 递归解法 """
#     def reverseList(self, head: ListNode) -> ListNode:
#         if not head:
#             return None
#         elif head.next:
#             reversed_ = p = self.reverseList(head.next)
#             while p.next:
#                 p = p.next
#             p.next = ListNode(head.val)
#             return reversed_
#         else:
#             return head


# @lc code=start
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """ 迭代解法 """
        p, q = None, head
        while q:
            r = q.next
            q.next = p
            p, q = q, r
        return p


# @lc code=end
if __name__ == "__main__":
    print(Solution().reverseList(None))
