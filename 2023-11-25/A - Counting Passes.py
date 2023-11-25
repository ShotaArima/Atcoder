n,l=input().split()
i=0
a=[int(i) for i in input().split()]

result=0

for i in range(len(a)):
    if a[i]>=int(l):
        result+=1

print(result)