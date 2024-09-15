class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ds = {}
        dt = {}

        for i in range(len(s)):
            if not s[i] in ds:
                ds[s[i]] = t[i]
            if not t[i] in dt:
                dt[t[i]] = s[i]

            if ds.get(s[i]) != t[i] or dt[t[i]] != s[i]:
                return False
        return True