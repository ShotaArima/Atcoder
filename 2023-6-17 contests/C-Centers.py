n = input()
a = list(map(int, input().split()))

memory = []
summary = []

for i in range(len(a)):
    if a[i] in memory and a[i] not in summary:
        summary.append(a[i])
    else:
        memory.append(a[i])

answer = ' '.join(map(str, summary))
print(answer)
