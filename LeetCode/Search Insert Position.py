class Solution:
    def searchInsert(self, nums, target):

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (r + l)//2
            if nums[m] < target:
                l += 1
            elif nums[m] > target:
                r -= 1
            else:
                return m
        return l