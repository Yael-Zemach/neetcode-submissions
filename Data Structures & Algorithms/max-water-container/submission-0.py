class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAr = 0
        l, r = 0, len(heights)-1
        while l<r:
            currMax = min(heights[l], heights[r])*(r-l)
            if currMax > maxAr:
                maxAr = currMax
            if heights[l] <=  heights[r]:
                l+=1
            else: r-=1
            
        return maxAr