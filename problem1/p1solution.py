#!/usr/bin/env python3


def two_sum(nums, target):
    """
    Given an array of integers, return indices of the two numbers such that
    they add up to a specific target.

    You may assume that each input would have exactly one solution, and you
    may not use the same element twice.

    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    diffs_idx = {}
    for i in range(len(nums)):
        if nums[i] in diffs_idx:
            return [diffs_idx[nums[i]], i]
        diffs_idx[target - nums[i]] = i


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    result = two_sum(nums, target)

    print("Two sum of", nums, "with target", target)
    print(result)
