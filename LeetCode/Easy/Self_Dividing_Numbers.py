class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        sDNs = []
        for x in range(left, right + 1):
            m = True
            s = set(int(i) for i in str(x))
            if 0 in s:
                continue
            for b in s:
                if x % b != 0:
                    m = False
            if m:
                sDNs.append(x)
        return sDNs
