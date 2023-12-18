# A phrase is a palindrome if, after converting all 
# uppercase letters into lowercase letters and removing
# all non-alphanumeric characters, it reads the same
# forward and backward. Alphanumeric characters include
# letters and numbers.
#
# Given a string s, return true if it is a palindrome,
# or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while True:
            while not s[left].isalnum():
                left += 1
                if left == len(s):
                    return True
            while not s[right].isalnum():
                right -= 1
                if right == -1:
                    return True

            if left >= right:
                return True

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

