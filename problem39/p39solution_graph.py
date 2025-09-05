from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Create graph from target value to 0 by subtracting candidate
        # values. If several paths lead to the same value we only need
        # to expand it once.
        parents = [[] for _ in range(target + 1)]
        stack = [target]

        while stack:
            node = stack.pop()
            for v in candidates:
                next_n = node - v
                if next_n >= 0:
                    if not parents[next_n]:  # Not visited yet
                        stack.append(next_n)
                    parents[next_n].append(node)

        # Reconstruct path sequence from 0
        solutions = set()
        r_stack = [(0, [])]
        while r_stack:
            node, seq = r_stack.pop()
            if node == target:
                seq.sort()
                solutions.add(tuple(seq))
            else:
                for p_node in parents[node]:
                    r_stack.append((p_node, [*seq, p_node - node]))

        return list(solutions)


if __name__ == "__main__":
    # nums = [8, 7, 4, 3]
    # target = 11
    nums = [2, 3, 6, 7]
    target = 7

    solution = Solution()
    result = solution.combinationSum(nums, target)

    print("Combination sums of:", nums)
    print("Target value:", target)
    print("")
    print(result)
