"""Given a string s containing just the characters '(', ')',
'{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

Example 4:
    Input: s = "([])"
    Output: true

Example 5:
    Input: s = "([)]"
    Output: false

Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
"""


class Solution:

    def isValid(self, s: str) -> bool:
        # Initialize with dummy value to avoid checking if it has elements
        last_open = [""]
        close_mapping = {")": "(", "]": "[", "}": "{"}

        for sym in s:
            if sym in close_mapping:
                if close_mapping[sym] != last_open.pop():
                    return False
            else:
                last_open.append(sym)

        # Remove dummy value and return
        last_open.pop()
        return not last_open


if __name__ == "__main__":
    strings = ["()", "()[]{}", "(]", "([])", "([)]"]
    expected = [True, True, False, True, False]

    solution = Solution()
    for s, e in zip(strings, expected, strict=True):
        r = solution.isValid(s)
        print(f"isValid('{s}') => {r}")
        print("   -", "OK" if r == e else "FAIL")
