"""Given an input string s and a pattern p, implement regular expression
matching with support for '.' and '*' where:

    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Example 1:
    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".

Example 2:
    Input: s = "aa", p = "a*"
    Output: true
    Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
    Input: s = "ab", p = ".*"
    Output: true
    Explanation: ".*" means "zero or more (*) of any character (.)".

Constraints:
    1 <= s.length <= 20
    1 <= p.length <= 20
    s contains only lowercase English letters.
    p contains only lowercase English letters, '.', and '*'.
    It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""


class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        return self._match_single(s, 0, p, 0)

    def _match_single(self, s: str, si: int, p: str, pi: int) -> bool:
        if pi >= len(p):
            return si == len(s)
        if pi < len(p) - 1 and p[pi + 1] == "*":
            return self._match_star(p[pi], s, si, p, pi + 2)
        if si < len(s) and (p[pi] == "." or p[pi] == s[si]):
            return self._match_single(s, si + 1, p, pi + 1)
        return False

    def _match_star(self, c: str, s: str, si: int, p: str, pi: int) -> bool:
        """Match zero or more `c` characters to `s` at `si`."""
        # Try matching 0, 1, 2 times and so on, at every try
        # we try again to continue doing single matching. Doing
        # it this way we use the star pattern to match the
        # minimum number of characters necessary to validate
        # if the sequence is a match.

        if self._match_single(s, si, p, pi):
            return True
        while si < len(s) and (c == "." or c == s[si]):
            si += 1
            if self._match_single(s, si, p, pi):
                return True

        return False


if __name__ == "__main__":
    sentence_and_patterns = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("hohohoo", "hohohoh*o", True),
        ("aaa", "a*a*a*", True),
        ("aaa", "ab*a*c*a", True),
        ("ab", ".*c", False),
    ]

    solution = Solution()
    for s, p, e in sentence_and_patterns:
        r = solution.isMatch(s, p)
        print("Sentence:", s)
        print("Pattern:", p)
        print("Is a match?", r)
        print("OK" if e == r else "FAIL")
        print("-" * 30)
