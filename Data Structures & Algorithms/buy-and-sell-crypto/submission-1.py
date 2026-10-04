class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxPro = 0
        while r < len(prices):
            if prices[r] - prices[l] > maxPro:
                maxPro = prices[r] - prices[l]
                r+=1
            elif prices[r] < prices[l]:
                l=r
                r=l+1
            else: 
                r+=1
        return maxPro


            
            


        