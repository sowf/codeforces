import math
import sys


input = lambda:sys.stdin.readline()


t = int(input().strip())


# VERDICT: TLE
for _ in range(t):
    n, k = [int(x.strip()) for x in input().split()]
    if k > math.log2(n):
        print(n+1)
    else:
        print(2**k)
