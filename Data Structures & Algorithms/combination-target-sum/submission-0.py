class Solution:
    def combinationSum(self, candidates, target):
        ans = []

        def backtrack(start, target, curr):
            if target == 0:
                ans.append(curr[:])
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                curr.append(candidates[i])

                backtrack(i, target - candidates[i], curr)

                curr.pop()

        backtrack(0, target, [])
        return ans