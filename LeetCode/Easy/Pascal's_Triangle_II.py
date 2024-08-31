class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        l = [1]
        for i in range(1,rowIndex+1):
            t = []
            t.append(1)
            for j in range(1,i):
                t.append(l[j-1]+l[j])
            t.append(1)
            l = t
        return l