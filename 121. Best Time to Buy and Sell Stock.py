class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        mini = prices[0]
        maxi = 0

        for p in prices[1:]:

            if p < mini:
                mini = p
                maxi = 0

            else:
                maxi = max(maxi, p)
                max_profit = max(max_profit, maxi - mini)

        return max_profit