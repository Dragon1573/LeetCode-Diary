""" HJ51 - 输出单向链表中倒数第k个结点

# 描述

输入一个单向链表，输出该链表中倒数第k个结点，链表的倒数第1个结点为链表的尾指针。

链表节点定义如下：

```cpp
struct ListNode {
    int m_nKey;
    ListNode *m_pNext;
};
```

正常返回倒数第k个结点指针，异常返回空指针。

数据范围：
    链表长度 1 <= n <= 1000
    目标索引 k <= n
    节点数据 0 <= val <= 10000

本题有多组输入。

# 输入说明

1. 输入链表节点个数
2. 输入链表的值
3. 输入 k 的值

# 输出描述

输出一个整数

# 示例

输入：
    8
    1 2 3 4 5 6 7 8
    4
输出：5
"""
from typing import Optional
from sys import stdin


class ListNode:
    def __init__(self, key: int, next: Optional['ListNode'] = None):
        self.key = key
        self.next = next


try:
    while True:
        # 头插法构造单链表，将链表元素倒序
        n = int(input())
        head = ListNode(0)
        for _ in input().strip().split():
            temp = ListNode(int(_), head.next)
            head.next = temp
        # 按链表串联顺序移动指针即可
        # 此时我们的链表与 OJ 输入链表相反
        k = int(input())
        p = head
        for _ in range(k):
            p = p.next
        print(p.key)
except Exception:
    pass
