# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return

        coffe = head
        while coffe.next:
            if coffe.val == coffe.next.val:
                coffe.next = coffe.next.next
            else:
                coffe = coffe.next

        return head