from typing import List


def peak_of_mountain_array(arr: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    l, r, idx = 0, len(arr) - 1, -1
    while l <= r:
        m = l + (r-l)//2
        if m == len(arr) - 1 or arr[m] > arr[m+1]:
            idx = m
            r = m - 1
        else:
            l = m + 1
    return idx


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = peak_of_mountain_array(arr)
    print(res)
