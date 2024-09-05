class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numdict = {}
        l = len(nums)/2
        maxlen = 0

        for num in nums:
            numdict[num] = numdict.get(num, 0) + 1
            if numdict[num] > maxlen:
                maxlen = numdict[num]
                the_guy = num
        return the_guy