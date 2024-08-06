class Solution:
    def mergeTwoLists(self,list1, list2):
        l = []
        s = []
        if len(list1) > len(list2):
            l = list1.copy()
            s = list2.copy()
        else:
            l = list2.copy()
            s = list1.copy()

        for x in s:
            coffe = True
            for i,n in enumerate(l):
                if x <= n:
                    l.insert(i, x)
                    coffe = False
                    break
        if coffe:
            l.append(x)

        return l