import sys

lines = [line for line in sys.stdin]
w = int(lines[0].strip())
print("YES" if w % 2 == 0 and w > 2 else "NO")
