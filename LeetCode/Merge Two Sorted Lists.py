class Solution(object):
    def mergeTwoLists(self, list1, list2):
        l = []
        s = []
        if len(list1) > len(list2):
            l = list2.copy()
            s = list1.copy()
        else:
            l = list1.copy()
            s = list2.copy()

        for i in s:
            for n in l:
                print("a")
                if not i > n:
                    inum = s.index(n) # index number
                    l.insert(inum,i)

        return l

list2 = [4,5,2,0]
list1 = [1,2,3,3]

print(Solution().mergeTwoLists(list1,list2))