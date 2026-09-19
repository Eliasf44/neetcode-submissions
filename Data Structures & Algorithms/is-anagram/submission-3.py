class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}


        for i in s:
            if i not in dic1:
                dic1[i] = 1
            else:
                dic1[i] += 1
        for q in t:
            if q not in dic2:
                dic2[q] = 1
            else:
                dic2[q] += 1
        
        if dic1 == dic2:
            return True
        
        return False