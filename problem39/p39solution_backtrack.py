from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = []
        path = []

        def back_track(start, curr):
            if curr == target:
                solutions.append(path[:])

            for i in range(start, len(candidates)):
                num = candidates[i]
                if curr + num <= target:
                    path.append(num)
                    back_track(i, curr + num)
                    path.pop()

        back_track(0, 0)

        return solutions


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
