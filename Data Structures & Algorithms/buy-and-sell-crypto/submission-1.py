class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Profit=[0]
        for i,num  in enumerate(prices):
             if i+1 < len(prices):
                Profit.append(max(0,max(prices[i+1:])-num))
        return max(Profit)
                

        