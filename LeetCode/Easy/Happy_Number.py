class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l = set()

        while n !=1:
            s = 0
            for x in str(n):
                s += int(x)**2
                
            if s in l: return False
            l.add(s)
            n=s

        return True