class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s=Counter(nums)
        for i,n in s.items():
            if(n==1):
                return i
        