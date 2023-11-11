class Solution:
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        if len(str1) != len(str2):
            return 0
        m1,m2 = {},{}
        for e1,e2 in zip(str1,str2):
            if e1 in m1 and m1[e1] != e2 or e2 in m2 and m2[e2] != e1:
                return 0
            m1[e1] = e2
            m2[e2] = e1
        return 1