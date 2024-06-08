class Solution:
    def longestCommonPrefix(self, strs):
        l = len(strs)
        samepre = ""
        samepre2 = ""
        for i in range(l):
            for j in range(i+1,l):
                control = 0
                if strs[i][control] == strs[j][control]:
                    samepre += strs[i][control]
                    control += 1
            if len(samepre) > len(samepre2):
                    samepre2 = samepre
        return samepre2


strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))