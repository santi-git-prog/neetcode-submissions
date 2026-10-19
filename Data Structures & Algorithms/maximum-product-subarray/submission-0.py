class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxi = nums[0]
        mini = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            if x < 0:
                maxi, mini = mini, maxi

            maxi = max(x, maxi * x)
            mini = min(x, mini * x)

            ans = max(ans, maxi)

        return ans