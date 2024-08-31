class Solution:
    def lengthOfLastWord(self, s):
        l = s.strip().split(" ")
        return len(l[-1])