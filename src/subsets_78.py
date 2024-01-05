# Given an integer array nums of unique elements,
# return all possible subsets (the power set).

# The solution set must not contain duplicate
# subsets. Return the solution in any order.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []

        subset = []
        def helper(i):
            if i >= len(nums):
                sol.append(subset.copy())
                return
            
            subset.append(nums[i])
            helper(i + 1)
            subset.pop()
            helper(i + 1)
        
        helper(0)
        
        return sol
