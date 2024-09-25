class Solution:
    def generateKey(self, num1, num2, num3):
        """
        :type num1: int
        :type num2: int
        :type num3: int
        :rtype: int
        """
        def zero(num):
            num = str(num)
            for i in range(4-len(num)):
                num = "0" + num
            return num

        num1 = zero(num1)
        num2 = zero(num2)
        num3 = zero(num3)

        keys = [0,0,0,0]
        key = ""
        for i in range(4):
            keys[i] = min(num1[i], num2[i], num3[i])

        for x in keys:
            key += x
        return int(key)