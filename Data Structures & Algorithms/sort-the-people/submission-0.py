class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        order = sorted(range(len(heights)), key=lambda i: heights[i], reverse=True)

        result = []

        for i in order:
            result.append(names[i])
        
        return result
        