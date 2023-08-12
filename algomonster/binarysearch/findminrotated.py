from typing import List


def find_min_rotated(arr: List[int]) -> int:
    l, r, idx = 0, len(arr) - 1, -1
    while l <= r:
        m = l + (r-l)//2
        if arr[m] <= arr[-1]:
            idx = m
            r = m - 1
        else:
            l = m + 1
    return idx


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = find_min_rotated(arr)
    print(res)
