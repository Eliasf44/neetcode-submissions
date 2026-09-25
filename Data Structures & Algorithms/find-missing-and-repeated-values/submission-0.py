class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)

        expected_sum = (n * n) * (n * n + 1) // 2
        actual_sum = 0 

        seen = set()
        repeated = 0

        for row in grid:
            for num in row:
                actual_sum += num

                if num in seen:
                    repeated = num
                
                seen.add(num)


        
        missing = expected_sum - (actual_sum - repeated)
        
        return [repeated, missing]