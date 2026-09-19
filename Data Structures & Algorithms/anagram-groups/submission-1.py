class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic1 = {}

        for i in strs:
            sort = "".join(sorted(i))

            if sort not in dic1:
                dic1[sort] = [i]
            else:
                dic1[sort].append(i)

        

        return list(dic1.values())
        