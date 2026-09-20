class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        subsets = [[]]
        start = 0

        for i in range(len(nums)):
            num = nums[i]
            prev = len(subsets)

            if i > 0 and nums[i] == nums[i - 1]:
                start = prev_old
            else:
                start = 0

            subsets += [current_sub + [num] for current_sub in subsets[start:]]

            prev_old = prev

        return subsets