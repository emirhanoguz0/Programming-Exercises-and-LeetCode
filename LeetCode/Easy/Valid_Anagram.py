class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l = []
        for x in s:
            l.append(x)

        for y in t:
            if y in l:
                l.remove(y)

        if l:
            return True
        else:
            return False