"""Write a function to find the longest common prefix string amongst an array
of strings.

If there is no common prefix, return an empty string "".

Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters if it is non-empty.
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        while True:
            for str in strs:
                if i >= len(str):
                    return str[:i]
                if strs[0][i] != str[i]:
                    return str[:i]
            i += 1


if __name__ == "__main__":
    inputs = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["pet", "pet"],
    ]
    outputs = ["fl", "", "pet"]

    solution = Solution()
    for strs, expected in zip(inputs, outputs, strict=True):
        prefix = solution.longestCommonPrefix(strs)
        print("Longest common prefix of:", strs)
        print("===", prefix, "===")
        print("OK" if prefix == expected else "FAIL")
