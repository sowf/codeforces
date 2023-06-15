import math
import sys


input = lambda:sys.stdin.readline()


t = int(input().strip())


# VERDICT: OK
for _ in range(t):
    n = int(input().strip())
    a = [int(x.strip()) for x in input().split()]
    if a[-1] == 1:
        print("NO")
    else:
        k=[]
        s=0
        y=0
        for i in range(n):
            if a[i]==1:
                s+=1
            else:
                k+=[s]
                k+=[0]*s
                s=0
            
        k.reverse()
        print("YES")
        print(*k)
