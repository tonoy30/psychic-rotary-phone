from typing import List


def first_not_smaller(arr: List[int], target: int) -> int:
    l, r, idx = 0, len(arr) - 1, -1
    while l <= r:
        m = l + (r-l)//2
        if arr[m] >= target:
            idx = m
            r = m - 1
        else:
            l = m + 1
    return idx


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = first_not_smaller(arr, target)
    print(res)
