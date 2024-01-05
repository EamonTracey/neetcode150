# Given an array of distinct integers candidates and
# a target integer target, return a list of all unique
# combinations of candidates where the chosen numbers
# sum to target. You may return the combinations in any order.
#
# The same number may be chosen from candidates an unlimited
# number of times. Two combinations are unique if the frequency
# of at least one of the chosen numbers is different.
#
# The test cases are generated such that the number of unique
# combinations that sum up to target is less than 150 combinations
# for the given input.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []

        comb = []
        s = 0
        def helper(i):
            nonlocal s

            if s == target:
                sol.append(comb.copy())
                return
            if s > target or i >= len(candidates):
                return
            
            comb.append(candidates[i])
            s += candidates[i]
            helper(i)
            s-= candidates[i]
            comb.pop()

            helper(i + 1)
        helper(0)

        return sol
