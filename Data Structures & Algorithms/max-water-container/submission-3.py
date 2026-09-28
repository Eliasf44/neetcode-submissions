class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        
        p1 = 0
        p2 = len(heights) - 1
        total = []
        currtotal = 0
        while p1 < p2:
            maxH = min(heights[p1], heights[p2])
            w = p2 - p1

            total.append(w * maxH)
            
            if heights[p1] < heights[p2]:
                p1+= 1
                
            else:
                p2 -= 1
                
                
        
        maxim = max(total)
        return(maxim)
