import sys
import itertools as it


# VERDICT: WA


def solution(arr1, arr2):
    res = []
    p1, p2 = 0, 0
    while p1 < len(arr1) and p2 < len(arr2):
        if res and res[-1] == arr2[p2]:
            res.append(arr2[p2])
            p2 += 1
        elif res and res[-1] == arr1[p1]:
            res.append(arr1[p1])
            p1 += 1
        elif arr1[p1] < arr2[p2]:
            res.append(arr1[p1])
            p1 += 1
        else:
            res.append(arr2[p2])
            p2 += 1
    
    while p1 < len(arr1):
        res.append(arr1[p1])
        p1 += 1

    while p2 < len(arr2):
        res.append(arr2[p2])
        p2 += 1

    counts = [sum(1 for _ in g) for k, g in it.groupby(res)]
    return max(counts)


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    b = list(map(int, sys.stdin.readline().strip().split()))
    print(solution(a, b))
