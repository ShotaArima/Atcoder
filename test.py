count = 0

for i in range(1, 10001):
    for j in range(1, 10001):
        k_square = i**2 + j**2
        k = int(k_square**0.5)
        if k**2 == k_square and i*j/2 <= 10000:
            count += 1

print(count)
