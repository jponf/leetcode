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

import itertools

from typing import List


class Solution:

    def __init__(self):
        self.cache = [[], ["()"]]

    def generateParenthesis(self, n: int) -> List[str]:
        if n < 1:
            return []

        if n < len(self.cache):
            return self.cache[n]

        p_prev = self.generateParenthesis(n - 1)
        parenthesis = [f"({p})" for p in p_prev]

        for i in range(1, n):
            j = n - i
            p_i = self.generateParenthesis(i)
            p_j = self.generateParenthesis(j)
            parenthesis.extend(map("".join, itertools.product(p_i, p_j)))

        self.cache.append(list(set(parenthesis)))
        return self.cache[-1]


if __name__ == "__main__":
    n = 4

    solution = Solution()
    print(f"Parenthesis({n}) =", solution.generateParenthesis(n))
