class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l = [[1]]

        for i in range(1, numRows):
            temp = [1]
            for j in range(1,i):
                temp.append(l[i-1][j-1]+l[i-1][j])
            temp.append(1)
            l.append(temp)

        return l