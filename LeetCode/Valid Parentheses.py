class Solution(object):
    def isValid(self, s):
        r = False
        list1 = ["(","{","["]
        list2 = [")","}","]"]

        l = list(s)
        if c in l in list1:
            i1 = list1.index()
            if list2[i] in l:
                i2 = list2.index()
                if i1 < i2:
                    r = True
        return r

s = [">£#$½{[]}"]
Solution().isValid(s)