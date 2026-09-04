class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (len(prices) == 1):
            return 0
        b = 0
        s = 1
        profit = max(0, prices[s] - prices[b])

        while b < len(prices)-1:
            if prices[s] <= prices[b]:
                b = s
                s += 1
            while s < len(prices) and prices[s] >= prices[b]:
                profit = max(profit, prices[s] - prices[b])
                s += 1

            b = s
            s += 1
        return profit