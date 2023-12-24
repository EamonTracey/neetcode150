# Given an array of strings strs, group the anagrams
# together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging
# the letters of a different word or phrase, typically
# using all the original letters exactly once.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def is_anagram(stra: str, strb: str) -> bool:
            if len(stra) != len(strb):
                return False
            seen = {}
            for char in stra:
                seen[char] = 1 + seen.get(char, 0)
            for char in strb:
                if char not in seen:
                    return False
                seen[char] -= 1
                if seen[char] == 0:
                    del seen[char]
            return not seen

        anagrams = []
        for s in strs:
            for i, a in enumerate(anagrams):
                if is_anagram(s, a[0]):
                    anagrams[i].append(s)
                    break
            else:
                anagrams.append([s])
        
        return anagrams

