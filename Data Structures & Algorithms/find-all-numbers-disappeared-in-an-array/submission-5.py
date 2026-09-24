class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        dic = {}
        out = []
 
        for i in nums:
            dic[i] = 1

        
        for i in range(1, len(nums) + 1):
            if i not in dic:
                out.append(i)


        return out