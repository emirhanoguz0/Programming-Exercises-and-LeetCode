class Solution:
    def longestCommonPrefix(self, strs):

        if len(strs) == 1 or len(strs) == 0:
            return strs[0]

        commonPre = ""
        shortstr = min(strs,key=len)
        strs.remove(shortstr)


        commonPre2 = "  " * len(shortstr)

        for str in strs:
            for i in range(len(shortstr)):
                if str[i] != shortstr[i]:
                    break
                commonPre += str[i]
            if len(commonPre) <= len(commonPre2):
                commonPre2 = commonPre
                commonPre = ""

        return commonPre2
