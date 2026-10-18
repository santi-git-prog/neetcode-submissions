
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = sorted(list(set(nums)))
        cnt = 1
        mcnt = 0
        i = 0

        while i < len(a):
            cnt = 1

            while i + 1 < len(a) and a[i + 1] == a[i] + 1:
                cnt += 1
                i += 1

            mcnt = max(mcnt, cnt)
            i += 1

        return mcnt
