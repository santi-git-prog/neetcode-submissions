class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s=Counter(nums)
        for i,a in s.items():
            if(a>1):
                return i
        