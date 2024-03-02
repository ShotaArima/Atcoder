import random

a, b = map(int, input().split())

while True:
    num = random.randint(0, 9)
    if num != a+b:
        break

print(num)