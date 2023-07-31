from typing import List


def binary_search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:  # <= because left and right could point to the same element, < would miss it
        m = l + (r-l)//2  # calculating the mid // for integer division
        # found the target, return its index
        if nums[m] == target:
            return m
        # middle element is less than target, discard left half by making left search boundary `mid + 1`
        elif nums[m] < target:
            l = m + 1
        # middle element is greater than target, discard right half by making right search boundary `mid - 1`
        else:
            r = m - 1
    return -1  # if we get here we don't hit above return so we don't find the target


if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = binary_search(arr, target)
    print(res)
