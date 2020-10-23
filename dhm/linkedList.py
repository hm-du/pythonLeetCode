'''
@author: ������룬��ԭ��
'''
from pip._internal.cli.cmdoptions import pre
from pip._vendor.requests.api import head
from _ast import If

# 1.��ת����https://leetcode-cn.com/problems/reverse-linked-list/
def reverseList(self, head):
    cur,prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev 

# 2.�������������еĽڵ㣺https://leetcode-cn.com/problems/swap-nodes-in-pairs/
def swapPairs(self, head):
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return self.next

# 3.��������https://leetcode-cn.com/problems/linked-list-cycle/
'''
���ֽⷨ
1. ��0.5s�ڱ������������ָ����û��Ϊnull�ġ����ַ�������ʵ�֣������ܲ�
2. ʹ��set�ṹ�����߹��Ľڵ��ַ�浽set�У�ÿ��һ���½ڵ����set�в��ң������set���Ѿ��иýڵ����ʾ�л�
3. ʹ�ÿ���ָ�룬��ָ������������ָ����һ�����������ָ���غ����ʾ�л�
'''
def hasCycle(self, head):
    fast = slow = head  #��ʼ������ָ��
    while slow and fast and fast.next: #�ж�slow��fast����ָ���Ƿ��ߵ��˵ף�����ߵ��׻�û����ײ��һ�𣬾ͷ���false����ʾû�л�
        slow = slow.next #��ָ����һ��
        fast = fast.next.next #��ָ��������
        if slow is fast: #������ָ����ײ��һ�����ʾ�л�������true
            return True
    return False

