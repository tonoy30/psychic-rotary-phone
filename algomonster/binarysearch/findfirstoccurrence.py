from typing import List


def find_first_occurrence(arr: List[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    idx, l, r = -1, 0, len(arr) - 1
    while l <= r:
        m = l + (r-l)//2
        if arr[m] == target:
            idx = m
            r = m - 1
        elif arr[m] > target:
            r = m - 1
        else:
            l = m + 1
    return idx


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = find_first_occurrence(arr, target)
    print(res)
