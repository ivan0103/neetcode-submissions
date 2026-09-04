class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        cur_max_profit = 0
        cur_min_price = prices[0]

        for day, price in enumerate(prices[1:]):
            if price < cur_min_price:
                cur_min_price = price

            if price - cur_min_price > cur_max_profit:
                cur_max_profit = price - cur_min_price

        if cur_max_profit <= 0:
            return 0

        return cur_max_profit