class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def solve(arr):
            a = 0
            b = 0

            for x in arr:
                c = max(a + x, b)
                a = b
                b = c

            return b

        return max(solve(nums[:-1]), solve(nums[1:]))