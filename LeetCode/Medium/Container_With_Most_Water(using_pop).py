class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        l = len(height)-1
        while l>0:
            if height[0]>height[-1]:
                m = height[-1]
                height.pop(-1)
            else:
                m = height[0]
                height.pop(0)

            area = (m*l)
            if  area > max_area:
                max_area = area
            l -= 1
        return max_area