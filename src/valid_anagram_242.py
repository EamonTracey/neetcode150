# Given two strings s and t, return true
# if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging
# the letters of a different word or phrase, typically
# using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1

        for char in t:
            if char not in counts or counts[char] == 0:
                return False
            counts[char] -= 1

        return True
