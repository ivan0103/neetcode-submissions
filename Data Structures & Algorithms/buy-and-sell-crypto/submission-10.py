class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]
        for i in prices:
            if (i < buy):
                buy = i
                continue
            sell = i
            res = max(res, sell - buy)
        return res