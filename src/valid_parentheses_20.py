# Given a string s containing just the characters
# '(', ')', '{', '}', '[' and ']', determine if the
# input string is valid.
# 
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        open_to_closed = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        stack = []

        for char in s:
            if char in open_to_closed:
                stack.append(char)
            elif len(stack) == 0:
                return False
            elif char != open_to_closed[stack.pop()]:
                return False

        return len(stack) == 0

