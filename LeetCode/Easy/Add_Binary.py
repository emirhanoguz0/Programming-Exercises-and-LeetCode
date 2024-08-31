class Solution:
    def addBinary(self, a, b):

        sum = 0
        sum += int(a,2)
        sum += int(b,2)

        binary = bin(sum)[2:]
        return str(binary)