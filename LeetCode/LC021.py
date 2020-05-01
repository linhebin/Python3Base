"""
21. 合并两个有序链表
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = p = ListNode(0)
        while l1 and l2:
            if l1.val >= l2.val:
                res.next = ListNode(l2.val)
                l2 = l2.next if l2 else 0
            else:
                res.next = ListNode(l1.val)
                l1 = l1.next if l1 else 0
            res = res.next
        if l1:
            while l1:
                res.next = ListNode(l1.val)
                l1 = l1.next if l1 else 0
                res = res.next
        if l2:
            while l2:
                res.next = ListNode(l2.val)
                l2 = l2.next if l2 else 0
                res = res.next
        return p.next
