from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        nums_len = len(nums)

        # Abort early
        # 1. Exactly 3 elements
        if nums_len == 3:
            return sum(nums)

        # 2. Min sum is larger than target
        if nums[0] + nums[1] + nums[2] >= target:
            return nums[0] + nums[1] + nums[2]

        # 3. Max sum is larger than target
        if nums[-3] + nums[-2] + nums[-1] <= target:
            return nums[-3] + nums[-2] + nums[-1]

        closest = nums[0] + nums[1] + nums[-1]
        closest_dist = abs(target - closest)

        for i in range(nums_len - 2):
            # Skip number if already tested
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Target is further away from min/max sum from i
            min_s = nums[i] + nums[i + 1] + nums[i + 2]
            max_s = nums[i] + nums[nums_len - 2] + nums[nums_len - 1]
            if target < min_s:
                min_s_d = abs(target - min_s)
                if min_s_d < closest_dist:
                    closest = min_s
                    closest_dist = min_s_d
            elif target > max_s:
                max_s_d = abs(target - max_s)
                if max_s_d < closest_dist:
                    closest = max_s
                    closest_dist = max_s_d
            else:
                # Find 2 sum closest to target - nums[i]
                t2sum = target - nums[i]
                v2sum = self.twoSumClosestSorted(nums, i + 1, nums_len - 1, t2sum)
                v3sum = nums[i] + v2sum
                d3sum = abs(target - v3sum)

                if d3sum < closest_dist:
                    closest = v3sum
                    closest_dist = d3sum

        return closest

    def twoSumClosestSorted(self, nums, left, right, target):
        best_s = nums[left] + nums[right]
        best_d = abs(target - best_s)

        while left < right:
            curr_s = nums[left] + nums[right]
            curr_d = abs(target - curr_s)
            if curr_d < best_d:
                best_s = curr_s
                best_d = curr_d

            if curr_s == target:
                return best_s
            elif curr_s > target:
                right -= 1
            else:
                left += 1

        return best_s


if __name__ == "__main__":
    nums = [-8, -3, -1, 2, 3, 4, 6, 8]
    target, expected = 7, 7

    # nums = [-1, 2, 1, -4]
    # target, expected = 1, 2

    # nums = [4, 0, 5, -5, 3, 3, 0, -4, -5]
    # target, expected = -2, -2

    # nums = [2, 3, 8, 9, 10]
    # target, expected = 16, 15

    solution = Solution()
    result = solution.threeSumClosest(nums, target)
    print("***", solution.threeSumClosest(nums, target))

    print("Target:", target)
    print("Expected:", expected)
    print("OK" if result == expected else "FAIL")
