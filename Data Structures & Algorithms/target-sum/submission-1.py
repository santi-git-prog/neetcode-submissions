class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={0:1}
        for i in nums:
            new={}
            for tot in dp:
                new[tot+i]=new.get(tot+i,0)+dp[tot]
                new[tot-i]=new.get(tot-i,0)+dp[tot]
            dp=new
        return dp.get(target,0)
