n = int(input())
a = []
tmp = []
for i in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp)

# print(f"a={a}")

# 各辺があるかを確認
tmp = []
ans = []
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            tmp.append(j+1)
    ans.append(tmp)
    tmp = []

for sublist in ans:
    print(" ".join(map(str, sublist)))