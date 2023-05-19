n, k = map(int, input().split())
a = list(map(int, input().split()))

product = 1
for num in a:
    product *= num

count = 0
while product % k == 0:
    product //= k
    count += 1

print(count)
