"""Given n pairs of parentheses, write a function to generate all
combinations of well-formed parentheses.

Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
    Input: n = 1
    Output: ["()"]


Constraints:
    1 <= n <= 8
"""

from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def _backtrack(opened: int, closed: int) -> None:
            if closed == n:
                result.append("".join(stack))

            if opened < n:
                stack.append("(")
                _backtrack(opened + 1, closed)
                stack.pop()
            if closed < opened:
                stack.append(")")
                _backtrack(opened, closed + 1)
                stack.pop()

        _backtrack(0, 0)
        return result


if __name__ == "__main__":
    n = 4

    solution = Solution()
    print(f"Parenthesis({n}) =", solution.generateParenthesis(n))
