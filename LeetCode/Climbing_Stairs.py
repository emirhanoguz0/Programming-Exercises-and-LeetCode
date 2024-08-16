class Solution:
    def climbStairs(self, n):

        if n <= 3:
            return n

        a = 1
        b = 2
        c = 0

        for i in range(3, n+1):
            c = a + b
            a = b
            b = c
        return c