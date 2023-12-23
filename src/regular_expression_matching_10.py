# Given an input string s and a pattern p,
# implement regular expression matching with
# support for '.' and '*' where:
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
# The matching should cover the entire input string (not partial).

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def match_helper(ids: int, idp: int) -> bool:
            if ids == len(s) and idp == len(p):
                return True

            if ids == len(s):
                if idp + 1 < len(p) and p[idp + 1] == "*":
                    return match_helper(ids, idp + 2)

            if ids >= len(s) or idp >= len(p):
                return False

            if idp + 1 < len(p) and p[idp + 1] == "*":
                if idp + 3 < len(p) and p[idp:idp + 2] == p[idp + 2:idp + 4]:
                    return match_helper(ids, idp + 2)
                if p[idp] != "." and s[ids] != p[idp]:
                    return match_helper(ids, idp + 2)
                return match_helper(ids, idp + 2) or match_helper(ids + 1, idp) or match_helper(ids + 1, idp + 2)

            if p[idp] == "." or s[ids] == p[idp]:
                return match_helper(ids + 1, idp + 1)

            return False

        return match_helper(0, 0)

