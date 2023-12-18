# Given an array of integers nums which is sorted
# in ascending order, and an integer target, write
# a function to search target in nums. If target
# exists, then return its index. Otherwise, return -1.
# 
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if target > nums[middle]:
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1
            else:
                return middle

        return -1

