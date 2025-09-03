"""
Problem: https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation:
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.

Example 2:
    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.

Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.

Constraints:
    3 <= nums.length <= 3000
    -105 <= nums[i] <= 105
"""

from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums_len = len(nums)
        results = []

        if nums[-1] < 0:
            return []

        start_r = nums_len - 1
        for i in range(nums_len - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0 or nums[i] + nums[i + 1] > 0 and nums[-1] > 0:
                break

            left = i + 1
            right = start_r

            # Update start_r for future iterations
            while start_r > left and nums[i] + nums[left] + nums[start_r] > 0:
                start_r -= 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return results


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    result = solution.threeSum(nums)

    print("Three sum of", nums)
    print(result)
