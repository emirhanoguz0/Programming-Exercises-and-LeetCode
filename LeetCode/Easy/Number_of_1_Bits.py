class Solution:
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = str(bin(n))
        c = 0

        for x in b[2:]:
            c += int(x)
        return c
