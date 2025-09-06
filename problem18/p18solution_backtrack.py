"""Given an array nums of n integers, return an array of all the unique
quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Example 1:
    Input: nums = [1,0,-1,0,-2,2], target = 0
    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
    Input: nums = [2,2,2,2,2], target = 8
    Output: [[2,2,2,2]]

Constraints:
    1 <= nums.length <= 200
    -109 <= nums[i] <= 109
    -109 <= target <= 109
"""

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        nums_len = len(nums)

        if len(nums) < 4:
            return []
        if len(nums) == 4:
            return [nums] if sum(nums) == target else []

        solutions = []
        summands = []

        def _back_track(start: int, k: int, curr: int):
            if k == 0 and curr == target:
                solutions.append(summands[:])
            elif k > 0:
                # Target not reachable
                min_s = curr + sum(nums[start + i] for i in range(k))
                if target < min_s:
                    return
                max_s = curr + sum(nums[nums_len - k + i] for i in range(k))
                if target > max_s:
                    return

                for i in range(start, nums_len - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    num = nums[i]
                    summands.append(num)
                    _back_track(i + 1, k - 1, curr + num)
                    summands.pop()

        _back_track(0, 4, 0)
        return solutions


if __name__ == "__main__":
    # nums = [1, 0, -1, 0, -2, 2]
    # target = 0
    # Expected: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

    # nums = [-1, 0, 1, 2, -1, -4]
    # target = -1
    # Expected: [[-4,0,1,2],[-1,-1,0,1]]

    nums = [-3, -2, -1, 0, 0, 1, 2, 3]
    target = 0
    # Expected: [[-3,-2,2,3], [-3,-1,1,3], [-3,0,0,3], [-3,0,1,2],
    #            [-2,-1,0,3], [-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]

    solution = Solution()
    result = solution.fourSum(nums, target)
    print("***", solution.fourSum(nums, target))

    print("Nums:", nums)
    print("Target:", target)
    print("Result:", result)
