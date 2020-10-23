'''
@author: 优秀代码，非原创
'''
from pip._internal.cli.cmdoptions import pre
from pip._vendor.requests.api import head
from _ast import If

# 1.反转链表：https://leetcode-cn.com/problems/reverse-linked-list/
def reverseList(self, head):
    cur,prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev 

# 2.两两交换链表中的节点：https://leetcode-cn.com/problems/swap-nodes-in-pairs/
def swapPairs(self, head):
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return self.next

# 3.环形链表：https://leetcode-cn.com/problems/linked-list-cycle/
'''
三种解法
1. 在0.5s内遍历链表，看后继指针有没有为null的。这种方法可以实现，但性能差
2. 使用set结构，将走过的节点地址存到set中，每到一个新节点就在set中查找，如果有set中已经有该节点则表示有环
3. 使用快慢指针，快指针走两步，慢指针走一步，如果快慢指针重合则表示有环
'''
def hasCycle(self, head):
    fast = slow = head  #初始化两个指针
    while slow and fast and fast.next: #判断slow、fast两个指针是否走到了底，如果走到底还没有碰撞在一起，就返回false，表示没有环
        slow = slow.next #慢指针走一步
        fast = fast.next.next #快指针走两步
        if slow is fast: #如两个指针碰撞在一起，则表示有环，返回true
            return True
    return False

