class Solution(object):
    def isValid(self, s):
        a = []
        for c in s:
            if c in "{[(":
                a.append(c)
            else:
                if not a or c == "}" and a[-1] != "{" or c == "]" and a[-1] != "[" or c == ")" and a[-1] != "(":
                    return False
                a.pop(-1)
        return not a

s = "["
print(Solution().isValid(s))