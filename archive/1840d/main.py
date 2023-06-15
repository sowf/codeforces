import functools
import sys
from statistics import mean



input = lambda:sys.stdin.readline()


t = int(input().strip())


@functools.lru_cache
def count_max_dev(arr, l, r):
    avg1, avg2, avg3 = int(mean(arr[:l])), int(mean(arr[l:r])), int(mean(arr[r:]))
    max_dev = max([
        max(arr[:l])-avg1, avg1-min(arr[:l]), 
        max(arr[l:r])-avg2, avg2-min(arr[l:r]),
        max(arr[r:])-avg3, avg3-min(arr[r:]),
    ])
    print(max(arr[:l])-avg1, avg1-min(arr[:l]))
    print(max(arr[l:r])-avg2, avg2-min(arr[l:r]))
    print(max(arr[r:])-avg3, avg3-min(arr[r:]))
    print(max_dev)

    print("-->", a[:l], a[l:r], a[r:])
    return max_dev


@functools.lru_cache
def get_new_indices(arr, l, r):
    if r - 1 <= l: return l, r

    cur_dev = count_max_dev(arr, l, r)
    l_dev = count_max_dev(arr, l+1, r)
    r_dev = count_max_dev(arr, l, r-1)
    # print(cur_dev, l, r, l_dev, r_dev)
    if cur_dev < l_dev and cur_dev < r_dev:
        return l, r
    elif l_dev < r_dev:
        return l+1, r
    else:
        return l, r-1


# VERDICT: 
for _ in range(t):
    n = int(input().strip())
    a = tuple(sorted({int(x.strip()) for x in input().split()}))

    if len(a) <= 3:
        print(0)
    else:
        n = len(a)
        l, r = 1, n-1
        while (l, r) != get_new_indices(a, l, r):
            l, r = get_new_indices(a, l, r)
        print(a[:l], a[l:r], a[r:])
