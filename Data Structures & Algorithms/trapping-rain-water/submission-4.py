class Solution:
    def trap(self, height: List[int]) -> int:
        output = 0 
        l = 0
        maxIdx = height.index(max(height))
        while l < maxIdx and height[l]< height[l+1]:
            l+=1
        r = l+1
        while r <= maxIdx:
            while r <= maxIdx and height[r]< height[l]:
                r+=1
            output += height[l]* (r-l-1)
            for i in range(r-l-1):
                output -= height[l+i+1]
            l=r
            r+=1
        l = len(height)-1
        while l > maxIdx and height[l]< height[l-1]:
            l-=1
        r = l-1
        while r >=maxIdx:
            while r >= maxIdx and height[r]< height[l]:
                r-=1
            output += height[l]* (l-r-1)
            for i in range(l-r-1):
                output -= height[r+i+1]
            l=r
            r-=1
        return output




            
        