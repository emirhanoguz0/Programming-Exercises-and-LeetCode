class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        s = 0
        for i in range(32):
            s = (s<<1) | (n & 1)
            n>>=1
        return s