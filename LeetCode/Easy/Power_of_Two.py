class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n % 2 != 0 or n==0:
            return False
        n /= 2
        return self.isPowerOfTwo(n)