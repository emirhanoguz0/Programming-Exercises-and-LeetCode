# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l = []
        while head is not None:
            if head.val in l:
                return True
            l.append(head.val)
            head = head.next
        return False