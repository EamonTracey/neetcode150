# Given an unsorted array of integers nums, return the
# length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sol = 0
        bounds = {}
        for num in nums:
            if num in bounds:
                continue

            if num - 1 not in bounds and num + 1 not in bounds:
                bounds[num] = (num, num)
            elif num - 1 in bounds and num + 1 not in bounds:
                bounds[num] = \
                bounds[bounds[num - 1][0]] = \
                (bounds[num - 1][0], num)
            elif num - 1 not in bounds and num + 1 in bounds:
                bounds[num] = \
                bounds[bounds[num + 1][1]] = \
                (num, bounds[num + 1][1])
            else:
                bounds[num] = \
                bounds[bounds[num - 1][0]] = \
                bounds[bounds[num + 1][1]] = \
                (bounds[num - 1][0], bounds[num + 1][1])
                
            sol = max(sol, 1 + bounds[num][1] - bounds[num][0])
        
        return sol
