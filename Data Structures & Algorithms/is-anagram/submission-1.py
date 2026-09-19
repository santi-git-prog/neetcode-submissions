class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        s.sort()
        t.sort()
        if(len(s)!=len(t)):
            return False
        for i,j in zip(s,t):
            if(i!=j):
                return False
        return True
                
        