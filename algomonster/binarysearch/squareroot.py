def square_root(n: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    if n == 0 or n == 1:
        return n
    l, r = 0, n
    while l <= r:
        m = l + (r-l)//2
        if m * m == n:
            return m
        elif m * m > n:
            r = m - 1
        else:
            l = m + 1
    return r


if __name__ == '__main__':
    n = int(input())
    res = square_root(n)
    print(res)
