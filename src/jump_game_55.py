# You are given an integer array nums. You are
# initially positioned at the array's first index,
# and each element in the array represents your
# maximum jump length at that position.

# Return true if you can reach the last index,
# or false otherwise.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {len(nums) - 1: True}
        def jump_helper(index: int) -> bool:
            if index in memo:
                return memo[index]
            if index >= len(nums):
                return False
            for jump in range(nums[index], 0, -1):
                if jump_helper(index + jump):
                    memo[index] = True
                    return memo[index]
            memo[index] = False
            return memo[index]

        return jump_helper(0)

