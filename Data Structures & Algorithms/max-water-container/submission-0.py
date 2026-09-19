class Solution:
    def maxArea(self, h: List[int]) -> int:
        i=0
        j=len(h)-1
        ans=0
        while(i<j):
            area=min(h[i],h[j])*(j-i)
            ans=max(area,ans)
            if(h[i]<h[j]):
                i+=1
            else:
                j-=1
        return ans
            


        