class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}

        for i in s:
            if i in dic1:
                dic1[i] += 1
            else:
                dic1[i] = 1
        
        for k in t:
            if k in dic2:
                dic2[k] += 1
            else:
                dic2[k] = 1
        
        if dic1 == dic2:
            return True
        return False