# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        mem = 0        
        head = None
        
        while l1 is not None or l2 is not None:
            l1_value = 0
            if l1 is not None:
                l1_value = l1.val
                l1 = l1.next
            l2_value = 0
            if l2 is not None:
                l2_value = l2.val
                l2 = l2.next
                
            if head is None:
                l3 = ListNode(l1_value + l2_value + mem)
                head = l3
            else:            
                l3.next = ListNode(l1_value + l2_value + mem)
                l3 = l3.next
            
            if l3.val >= 10:
                mem = 1
                l3.val %= 10
            else:
                mem = 0
                
        if mem > 0:
            l3.next = ListNode(mem)
            
        return head
        