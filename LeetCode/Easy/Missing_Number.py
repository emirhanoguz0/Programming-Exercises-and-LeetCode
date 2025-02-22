class Solution():
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        nums_len = len(nums)

        sum = (nums_len * (nums_len +1))/2

        for num in nums:
            sum -= num

        return sum