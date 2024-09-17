class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        if n < 1:
            return False
        n /= 2
        print(n)
        return self.isPowerOfTwo(n)

print(Solution().isPowerOfTwo(3))