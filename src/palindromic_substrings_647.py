# Given a string s, return the number of
# palindromic substrings in it.
#
# A string is a palindrome when it reads
# the same backward as forward.
#
# A substring is a contiguous sequence
# of characters within the string.

class Solution:
    def countSubstrings(self, s: str) -> int:
        sol = 0

        i = 0
        while i < len(s):
            sol += 1

            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                sol += 1
                left -= 1
                right += 1
            
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                sol += 1
                left -= 1
                right += 1
            
            i += 1
        
        return sol

