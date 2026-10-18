
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        cnt = Counter(t)
        l = 0
        need = len(t)
        start = 0
        minlen = float('inf')

        for r in range(len(s)):
            if cnt[s[r]] > 0:
                need -= 1

            cnt[s[r]] -= 1

            while need == 0:
                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    start = l

                cnt[s[l]] += 1

                if cnt[s[l]] > 0:
                    need += 1

                l += 1

        if minlen == float('inf'):
            return ""

        return s[start:start + minlen]
