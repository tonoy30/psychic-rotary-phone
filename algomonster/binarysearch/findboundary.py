from typing import List


def find_boundary(nums: List[bool]) -> int:
    boundary_idx, l, r = -1, 0, len(nums) - 1
    while l <= r:
        m = l + (r-l)//2
        if nums[m]:
            boundary_idx = m
            r = m - 1
        else:
            l = m + 1
    return boundary_idx
