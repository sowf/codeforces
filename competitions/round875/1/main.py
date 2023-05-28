import sys


# VERDICT: RE


def solution(lst):
    n = len(lst)

    b = []
    a = sorted(lst, reverse=True)
    ab = list(lst)

    for i in range(n-1, -1, -1):
        if i == n - 1:
            max_val = a.pop(0)
            ab[i] += max_val
            b.append(max_val)
        else:
            l = 0
            while ab[i] + a[l] > ab[i+1]:
                l += 1

            cur_val = a.pop(l)
            ab[i] += cur_val
            b.append(cur_val)

    return b[::-1]

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    print(" ".join(map(str, solution(arr))))
