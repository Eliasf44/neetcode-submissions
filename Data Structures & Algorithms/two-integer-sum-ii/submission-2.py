class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        bot = 0

        top = len(numbers) - 1

        ret = [numbers[bot], numbers[top]]

        while (numbers[bot] + numbers[top]) != target:
            if target > numbers[bot] + numbers[top]:
                bot += 1
            else:
                top -= 1
        
        return [bot + 1, top +1 ]