class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)

        a = 0
        b = 0

        for i in range(2, n + 1):
            c = min(a + cost[i-2], b + cost[i-1])
            a = b
            b = c

        return b