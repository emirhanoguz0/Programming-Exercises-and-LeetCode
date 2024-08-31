class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        sugar = ListNode()
        salt = sugar

        while list1 and list2:
            if list1.val < list2.val:
                sugar.next = list1
                list1 = list1.next
            else:
                sugar.next = list2
                list2 = list2.next
            sugar = sugar.next

        if list1:
            sugar.next = list1
        else:
            sugar.next = list2

        return salt.next