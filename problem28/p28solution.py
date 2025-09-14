"""Given two strings needle and haystack, return the index of the first
occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0
    Explanation: "sad" occurs at index 0 and 6.
    The first occurrence is at index 0, so we return 0.

Example 2:
    Input: haystack = "leetcode", needle = "leeto"
    Output: -1
    Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:
    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Python built-in
        # return haystack.find(needle)

        needle_len = len(needle)
        for i in range(len(haystack) - needle_len + 1):
            # Using substrings
            if haystack[i : i + needle_len] == needle:
                return i

            # Without Python slicing
            # found = True
            # for j, c in enumerate(needle):
            #     if haystack[i + j] != c:
            #         found = False
            #         break
            # if found:
            #     return i

        return -1


if __name__ == "__main__":
    haystack = "sadbutsad"
    needle = "sad"

    solution = Solution()
    idx = solution.strStr(haystack, needle)
    if idx > -1:
        print(f"First occurrence of {needle} in {haystack} is at {idx}")
    else:
        print(f"'{needle} does not appear in {haystack}")
