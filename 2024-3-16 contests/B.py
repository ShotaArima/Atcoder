import math

x = int(input())
result = math.ceil(x//10)
if x % 10 != 0:
    result += 1
print(result)
