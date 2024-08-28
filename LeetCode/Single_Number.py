class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while True:
            n = nums[0]
            if n in nums[1:]:
                nums.remove(n)
                nums.remove(n)
            else:
                return n