class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        dic1 = {}

        for i in strs:
            sort = "".join(sorted(i))

            if sort not in dic1:
                dic1[sort] = [i]
            else:
                dic1[sort].append(i)

        

        for value in dic1.values():
            out.append(value)



        return out
        