from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.kSum(nums, target, 4)

    def kSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        nums.sort()
        return self._kSumSorted(
            nums=nums,
            target=target,
            left=0,
            k=k,
        )

    def _kSumSorted(self, nums, target, left, k):
        nums_len = len(nums)
        if nums_len - left >= k:
            # Target not reachable
            min_s = sum(nums[left + i] for i in range(k))
            if target < min_s:
                return []
            max_s = sum(nums[nums_len - k + i] for i in range(k))
            if target > max_s:
                return []

            # Two sum variant or recursive k-sum
            if k == 2:
                return self.twoSumSorted(nums, target, left, nums_len - 1)
            else:
                solutions = []
                for i in range(left, nums_len + 1 - k):
                    if i > left and nums[i] == nums[i - 1]:
                        continue

                    num = nums[i]
                    for solution in self._kSumSorted(
                        nums=nums,
                        target=target - num,
                        left=i + 1,
                        k=k - 1,
                    ):
                        solution.append(num)
                        solutions.append(solution)
                return solutions
        elif len(nums) == k:
            return [nums[:]]

        return []

    def twoSumSorted(self, nums, target, left, right):
        pairs = []
        while left < right:
            s = nums[left] + nums[right]
            if s < target:
                left += 1
            elif s > target:
                right -= 1
            else:
                pairs.append([nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left - 1] == nums[left]:
                    left += 1
                while left < right and nums[right + 1] == nums[right]:
                    right -= 1

        return pairs


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
