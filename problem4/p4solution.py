#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def find_sorted_arrays_median(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    if len(nums1) > len(nums2):
        return _find_sorted_ararys_median(nums2, 0, len(nums2), nums1, 0, len(nums1))

    return _find_sorted_ararys_median(nums1, 0, len(nums1), nums2, 0, len(nums2))


def find_sorted_array_median(nums):
    """
    :type nums: List[int]
    :rtype: float
    """
    mid = len(nums) // 2
    return nums[mid] if len(nums) % 2 else (nums[mid - 1] + nums[mid]) / 2.0


def _find_sorted_ararys_median(nums1, start1, len1, nums2, start2, len2):
    mid2 = start2 + len2 // 2

    if len1 == 0:
        return nums2[mid2] if len2 % 2 else (nums2[mid2 - 1] + nums2[mid2]) / 2.0
    if len1 == 1:
        if len2 == 1:
            return (nums1[start1] + nums2[start2]) / 2.0
        elif len2 % 2:  # is odd
            return median_of_4(
                nums1[start1], nums2[mid2 - 1], nums2[mid2], nums2[mid2 + 1]
            )
        else:  # is even
            return median_of_3(nums1[start1], nums2[mid2 - 1], nums2[mid2])
    elif len1 == 2:
        if len2 == 2:
            return median_of_4(
                nums1[start1], nums1[start1 + 1], nums2[start2], nums2[start2 + 1]
            )
        elif len2 % 2:  # is odd
            return median_of_3(
                max(nums1[start1], nums2[mid2 - 1]),
                nums2[mid2],
                min(nums1[start1 + 1], nums2[mid2 + 1]),
            )
        else:  # is even
            return median_of_4(
                max(nums1[start1], nums2[mid2 - 2]),
                nums2[mid2 - 1],
                nums2[mid2],
                min(nums1[start1 + 1], nums2[mid2 + 1]),
            )

    idx1, idx2 = start1 + (len1 - 1) // 2, start2 + (len2 - 1) // 2
    if nums1[idx1] > nums2[idx2]:
        return _find_sorted_ararys_median(
            nums1,
            start1,
            len1 // 2 + 1,
            nums2,
            start2 + idx1 - start1,
            len2 + start1 - idx1,
        )
    else:
        return _find_sorted_ararys_median(
            nums1, idx1, len1 // 2 + 1, nums2, start2, len2 + start1 - idx1
        )


def median_of_2(num1, num2):
    """Utility functions to compute the median of 3 numbers"""
    return (num1 + num2) / 2.0


def median_of_3(num1, num2, num3):
    """Utility functions to compute the median of 3 numbers"""
    return num1 + num2 + num3 - min(num1, num2, num3) - max(num1, num2, num3)


def median_of_4(num1, num2, num3, num4):
    """Utility functions to compute the median of 4 numbers"""
    num_sum = num1 + num2 + num3 + num4
    num_sum -= min(num1, num2, num3, num4)
    num_sum -= max(num1, num2, num3, num4)
    return num_sum / 2.0


if __name__ == "__main__":
    NUMS1 = [1, 3]
    NUMS2 = [2]
    print("Median of", NUMS1, "and", NUMS2)
    print(" > Expected:", find_sorted_array_median(sorted(NUMS1 + NUMS2)))
    print(" > Result:", find_sorted_arrays_median(NUMS1, NUMS2))

    NUMS3 = [1, 2]
    NUMS4 = [3, 4]
    print("Median of", NUMS3, "and", NUMS4)
    print(" > Expected:", find_sorted_array_median(sorted(NUMS3 + NUMS4)))
    print(" > Result:", find_sorted_arrays_median(NUMS3, NUMS4))

    NUMS5 = [1, 2]
    NUMS6 = [3, 4, 5]
    print("Median of", NUMS5, "and", NUMS6)
    print(" > Expected:", find_sorted_array_median(sorted(NUMS5 + NUMS6)))
    print(" > Result:", find_sorted_arrays_median(NUMS5, NUMS6))

    NUMS7 = [1, 2, 5, 8, 10]
    NUMS8 = [3, 4, 6, 9, 12]
    print("Median of", NUMS7, "and", NUMS8)
    print(" > Expected:", find_sorted_array_median(sorted(NUMS7 + NUMS8)))
    print(" > Result:", find_sorted_arrays_median(NUMS7, NUMS8))

    NUMS9 = [1, 2, 5, 8, 10]
    NUMS10 = [2, 3, 4, 6, 9, 12]
    print("Median of", NUMS9, "and", NUMS10)
    print(" > Expected:", find_sorted_array_median(sorted(NUMS9 + NUMS10)))
    print(" > Result:", find_sorted_arrays_median(NUMS9, NUMS10))

    NUMS11 = [1]
    NUMS12 = [4, 7, 10, 15]
    print("Median of", NUMS11, "and", NUMS12)
    print(" > Expected:", find_sorted_array_median(sorted(NUMS11 + NUMS12)))
    print(" > Result:", find_sorted_arrays_median(NUMS11, NUMS12))

    NUMS13 = [1]
    NUMS14 = [4, 7, 10]
    print("Median of", NUMS13, "and", NUMS14)
    print(" > Expected:", find_sorted_array_median(sorted(NUMS13 + NUMS14)))
    print(" > Result:", find_sorted_arrays_median(NUMS13, NUMS14))

    NUMS15 = [1, 5, 6]
    NUMS16 = [2, 3, 4, 7, 8]
    print("Median of", NUMS15, "and", NUMS16)
    print(" > Expected:", find_sorted_array_median(sorted(NUMS15 + NUMS16)))
    print(" > Result:", find_sorted_arrays_median(NUMS15, NUMS16))

    NUMS17 = []
    NUMS18 = [2, 3]
    print("Median of", NUMS17, "and", NUMS18)
    print(" > Expected:", find_sorted_array_median(sorted(NUMS17 + NUMS18)))
    print(" > Result:", find_sorted_arrays_median(NUMS17, NUMS18))
