class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)-1,-1,-1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
                continue
            else:
                break
        if digits[0] == 0:
            digits.insert(0,1)
        return digits