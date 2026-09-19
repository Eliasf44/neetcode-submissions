class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        

        for i, num in enumerate(nums):
            hmap[num] = i

        
        for i, num in enumerate(nums):
            desired = target - num

            if desired in hmap and hmap[desired] != i:
                return [i, hmap[desired]]

        

