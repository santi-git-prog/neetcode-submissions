
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        maxf = max(cnt.values())
        count = list(cnt.values()).count(maxf)

        return max(len(tasks), (maxf - 1) * (n + 1) + count)
