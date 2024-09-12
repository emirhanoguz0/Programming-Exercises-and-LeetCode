class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i,max_area = 0,0
        j = len(height) - 1

        while i<j:
            m = min(height[i], height[j])
            area = (j-i) * m

            if  area > max_area:
                max_area = area

            elif m == height[i]:
                i += 1
            else:
                j -= 1

        return max_area