# Given a string s, find the length of the longest
# substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sol = 0

        left = 0
        right = 0
        seen = set()
        for right in range(len(s)):
            if s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            sol = max(sol, right - left + 1)

        return sol

