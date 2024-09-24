class Solution(object):
    def losingPlayer(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: str
        """
        turn = min(x,y/4)

        if turn % 2 == 0:
            return "Bob"
        else:
            return "Alice"