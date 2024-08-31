# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def realnumbers(self,l):
        a = ""
        while l:
            a+=str(l.val)
            l=l.next
        return int(a[::-1])

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        summ = self.realnumbers(l1) + self.realnumbers(l2)
        str_sum = str(summ)[::-1]

        l3 = ListNode(int(str_sum[0]))
        temp = l3

        for x in str_sum[1:]:
            temp.next = ListNode(int(x))
            temp = temp.next

        return l3