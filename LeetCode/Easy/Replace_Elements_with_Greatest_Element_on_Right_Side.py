class Solution:
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        max_val = max(arr)
        for i in range(len(arr) - 1):
            if arr[i] != max_val:
                arr[i] = max(arr[i:])
            else:
                max_val = max(arr[i+1:])
                arr[i] = max_val
        arr[-1] = -1
        return arr