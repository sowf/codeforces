import sys
input = lambda:sys.stdin.readline()


t = int(input().strip())


# VERDICT: TLE
for _ in range(t):
    n, k = [int(x.strip()) for x in input().split()]
    print(min((2**k, n+1)))
