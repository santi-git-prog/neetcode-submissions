class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        x=list(permutations(nums))
        y=[]
        for i in x:
            y.append(list(i))
        return y

        