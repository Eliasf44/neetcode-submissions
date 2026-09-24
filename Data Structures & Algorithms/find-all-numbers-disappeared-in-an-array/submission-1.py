class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)

        dic = {}
        out = []
 
        for i in nums:
            dic[i] = 1

        
        for i in range(1, length + 1):
            if i not in dic:
                out.append(i)


        return out