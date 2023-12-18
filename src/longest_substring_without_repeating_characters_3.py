# Given a string s, find the length of the longest
# substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for left in range(len(s)):
            seen = set()
            right = left
            length = 0
            while right < len(s):
                if s[right] in seen:
                    break
                seen.add(s[right])
                length += 1
                max_length = max(max_length, length)
                right += 1

        return max_length

