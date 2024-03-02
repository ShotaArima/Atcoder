n, q = map(int, input().split())
a = list(map(int, input().split()))
query = [tuple(map(int, input().split())) for _ in range(q)]
num,s, e = zip(*query)

for i in range(q):
    tmp = a[s[i]]
    for j in range(s[i]+1, e[i]):
        if tmp < a[j]:
            tmp = a[j]
        print(tmp)