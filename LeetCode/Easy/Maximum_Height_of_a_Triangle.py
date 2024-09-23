class Solution(object):
    def maxHeightOfTriangle(self, red, blue):
        """
        :type red: int
        :type blue: int
        :rtype: int
        """
        def helper(top,bottom):
            flor = 0
            ball = 1
            while True:
                if top >= ball:
                    flor += 1
                    top -= ball
                    ball += 1

                    if bottom >= ball:
                        flor += 1
                        bottom -= ball
                        ball += 1
                    else:
                        return flor
                else:
                    return flor

        a1 = helper(red,blue)
        a2 = helper(blue,red)

        if a1 > a2:
            return a1
        else:
            return a2