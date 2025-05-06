class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        min_p = prices[0]
        max_p = 0
        for el in prices:
            min_p = min(min_p, el)
            diff = el - min_p
            max_p = max(max_p, diff)
        return max_p


            