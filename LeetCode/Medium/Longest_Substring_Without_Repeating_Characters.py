class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = []
        maxlen = 0

        for i in range(len(s)):
            if s[i] not in l:
                l.append(s[i])
            else:
                if len(l) > maxlen:
                    maxlen = len(l)
                while s[i] in l:
                    l.pop(0)
                l.append(s[i])

        if len(l) > maxlen:
            maxlen = len(l)

        return maxlen