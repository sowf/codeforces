# ''' # FASTIO  BEGINS 0.87 sec
import sys
input=lambda:sys.stdin.readline()
# FASTIO  ENDS '''

y0, y1 = [int(x) for x in input().split()]
c = sum(not int(input()) % y1 for i in range(y0))
print(c)
