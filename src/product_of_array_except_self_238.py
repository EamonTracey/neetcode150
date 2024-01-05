# Given an integer array nums, return an array answer
# such that answer[i] is equal to the product of all
# the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is
# guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time
# and without using the division operation.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        for i, num in enumerate(nums[:-1]):
            pre.append(num * pre[i])
        post = [1]
        for i, num in enumerate(reversed(nums[1:])):
            post.append(num * post[i])
        
        sol = []
        for i in range(len(nums)):
            sol.append(pre[i] * post[len(nums) - 1 - i])
        
        return sol
