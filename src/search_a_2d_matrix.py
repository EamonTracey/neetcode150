# You are given an m x n integer matrix matrix with
# the following two properties:
# 1. Each row is sorted in non-decreasing order.
# 2. The first integer of each row is greater than
# the last integer of the previous row.
#
# Given an integer target, return true if target is
# in matrix or false otherwise.
#
# You must write a solution in O(log(m * n)) time complexity.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        row = None
        while left <= right:
            middle = (left + right) // 2

            if target < matrix[middle][0]:
                right = middle - 1
            elif target > matrix[middle][-1]:
                left = middle + 1
            else:
                row = middle
                break

        if row is None:
            return False

        left = 0
        right = len(matrix[0]) - 1
        row = matrix[row]
        while left <= right:
            middle = (left + right) // 2

            if target < row[middle]:
                right = middle - 1
            elif target > row[middle]:
                left = middle + 1
            else:
                return True

        return False
