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
        coffe = head
        me = head

        while coffe and coffe.next:
            coffe = coffe.next.next
            me = me.next

            if coffe == me:
                return True

        return False