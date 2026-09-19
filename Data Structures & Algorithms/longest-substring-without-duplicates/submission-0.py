class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = set()
        l = 0
        maxi = 0
        
        for r in range(len(s)):
   
            while s[r] in c:
                c.remove(s[l])
                l += 1
                
            
            c.add(s[r])
            maxi = max(maxi, r - l + 1)
            
        return maxi