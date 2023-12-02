from bisect import bisect_right

n = int(input())
a = list(map(int, input().split()))

# 各要素より右にある要素を昇順にソート
sorted_a = sorted(a)

# 各要素に対して、それより大きい要素の和を求める
result = [0] * n
for i in range(n):
    index = bisect_right(sorted_a, a[i])
    if index < n:
        result[i] = sum(sorted_a[index:])

print(*result)
