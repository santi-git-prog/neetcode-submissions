class Solution:
    def rob(self, nums: list[int]) -> int:
        a = 0
        b = 0

        for i in range(len(nums)):
            c = max(a + nums[i], b)
            a = b
            b = c

        return b