n,s=map(int,input().split())
nums = list(map(int, input().split()))

print(f"n={n}, s={s}")
for i in range(n):
    print(nums[i])

for i in range(n):
    for j in range(n):
        print(f"{i}+{j}={i+j}")