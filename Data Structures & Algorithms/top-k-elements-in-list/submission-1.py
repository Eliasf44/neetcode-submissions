class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic1={}

        for i in nums:
            if i not in dic1:
                dic1[i] = 1
            else:
                dic1[i] += 1
        

        freq = [[] for _ in range(len(nums)+1)]

        for num, count in dic1.items():
            freq[count].append(num)

        result = []

        for count in range(len(freq) - 1, 0, -1):
            for num in freq[count]:
                result.append(num)

                if len(result) == k:
                    return result
        