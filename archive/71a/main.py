import sys

lines = [line for line in sys.stdin]

words = [w.strip() for w in lines[1:]]
for word in words:
    n = len(word)
    if n <= 10:
        print(word)
    else:
        print(f"{word[0]}{n-2}{word[-1]}")
