from collections import Counter

n, t = map(int, input().split())

ab = [map(int, input().split()) for _ in range(t)]
a, b = zip(*ab)


s = [0] * n

for i in range(t):
    s[a[i]-1] += b[i]
    count = len(Counter(s).keys())
    print(count)
