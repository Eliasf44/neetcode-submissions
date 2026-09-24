class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic1 = {}

        for i in nums:
            if i not in dic1:
                dic1[i] = 1
            else:
                dic1[i] += 1

            if dic1[i] > len(nums) / 2:
                return i 
                