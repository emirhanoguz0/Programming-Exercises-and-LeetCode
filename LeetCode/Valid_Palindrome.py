class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp ="".join(x for x in s if x.isalnum()).lower()
        return temp == temp[::-1]