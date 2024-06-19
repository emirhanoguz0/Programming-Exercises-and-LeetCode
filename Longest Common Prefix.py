class Solution:
    def longestCommonPrefix(self, strs):
        commonPre = ""
        commonPre2 = "  " * len(strs)

        shortstr = min(strs,key=len)
        strs.remove(shortstr)

        for str in strs:
            for i in range(len(shortstr)):
                if str[i] == shortstr[i]:
                    commonPre += str[i]
            if len(commonPre) < len(commonPre2):
                commonPre2 = commonPre

        return commonPre2

strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))