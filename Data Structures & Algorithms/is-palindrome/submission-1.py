class Solution:
    def isPalindrome(self, s: str) -> bool:
        fins=""
        for i in s:
            if(i.isalnum()):
                if(i.isalpha()):
                    fins+=i.lower()
                else:
                    fins+=i
        print(fins)
        return fins==fins[::-1]
        