class Solution:
    def longestCommonPrefix(self, strs):
        l = len(strs)
        samepre2 = ""
        for i in range(l):
            print(i)
            samepre = ""
            for j in range(i+1,l):
                print(f"{j}j")
                for control in range(len(strs[i])):
                    if strs[i][control] != strs[j][control]:
                        break
                    else:
                        samepre += strs[i][control]
            if len(samepre) > len(samepre2):
                    samepre2 = samepre
        return samepre2

strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))