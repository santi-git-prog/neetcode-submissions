class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pri=float('inf')
        pro=0
        for i in prices:
            if(i<pri):
                pri=i
            elif(i-pri>pro):
                pro=i-pri
        return pro        