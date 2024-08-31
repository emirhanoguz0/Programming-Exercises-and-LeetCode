# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        temp1 = root
        temp2 = root

        while temp1 and temp2:
            if temp1.left != temp2.right:
                return False
            if temp1.right != temp2.left:
                return False