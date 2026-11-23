class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        doc={}
        for i,num in enumerate(nums):
            c=target-num
            if c in doc:
                return [doc[c],i]
            doc[num]=i
        
        