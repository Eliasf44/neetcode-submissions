class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        odd = 0 
        even = 0



        for i in range(1, len(nums)):
            if nums[i-1] & 1 == nums[i] & 1:
                return False
            
        return True



        
        