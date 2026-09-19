class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=Counter(nums)
        for i,a in a.items():
            if(a>1):
                return True
        return False
        