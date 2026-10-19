class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        if n == 0:
            return 0

        dp = [0] * n
        buy = -prices[0]

        for i in range(1, n):
            if i >= 2:
                buy = max(buy, dp[i-2] - prices[i])
            else:
                buy = max(buy, -prices[i])

            dp[i] = max(dp[i-1], buy + prices[i])

        return dp[n-1]