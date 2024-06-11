class Solution:
    def longestCommonPrefix(self, strs):

        shortstr = min(strs,key=len)
        strs.remove(shortstr)
        for i, ch in shortstr:
            if str[]

strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))