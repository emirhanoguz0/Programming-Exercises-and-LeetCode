class Solution(object):
    def twoSum(self, nums, target):
        l=len(nums)
        j = 0
        for i in range(l):
            for j in range(i+1,l):
                if target == nums[i] + nums[j]:
                    return i,j