class Solution:
    def get_all_subsets_iterative(self,nums):
        subsets = [[]] 
        for num in nums:
            subsets += [current_sub + [num] for current_sub in subsets]
        return subsets
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.get_all_subsets_iterative(nums)
        
        