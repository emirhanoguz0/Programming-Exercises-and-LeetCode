class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        nums = {}
        l = []
        for num in arr:
            if num not in nums:
                nums[num] = 1
            else:
                nums[num] += 1

        l = list(nums.values())

        if len(l) == len(set(l)):
            return True
        else:
            return False