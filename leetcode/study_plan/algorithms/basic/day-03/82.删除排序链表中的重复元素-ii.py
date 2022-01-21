#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (53.18%)
# Likes:    777
# Dislikes: 0
# Total Accepted:    208.3K
# Total Submissions: 391.7K
# Testcase Example:  '[1, 2, 3, 3, 4, 4, 5]'
#
# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。
#
# 返回同样按升序排列的结果链表。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
#
#
# 示例 2：
#
#
# 输入：head = [1,1,1,2,3]
# 输出：[2,3]
#
#
#
#
# 提示：
#
#
# 链表中节点数目在范围 [0, 300] 内
# -100 <= Node.val <= 100
# 题目数据保证链表已经按升序排列
#
#
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        array = []
        while self:
            array.append(self.val)
            self = self.next
        return str(array)


# @lc code=start
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            # 空链表
            return head
        # 辅助哑结点
        current = dummy = ListNode(next=head)
        while current.next and current.next.next:
            # 链表至少存在2个结点
            if current.next.val == current.next.next.val:
                # 连续2个节点存在重复
                x = current.next.val
                while current.next and current.next.val == x:
                    # 移除后续的一个节点
                    current.next = current.next.next
            else:
                # 下一个节点不重复，添加到链表中
                current = current.next
        # 跳过哑节点
        return dummy.next


# @lc code=end
