class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      L=0
      R=1
      MaxProfit=0
      while(R <len(prices)):
        if (prices[L]>=prices[R]):
            L=R
            R+=1
        else:
            MaxProfit=max(MaxProfit,prices[R]-prices[L])
            R+=1
      return MaxProfit


        