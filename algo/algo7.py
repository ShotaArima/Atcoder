count=0
num=input().split()
n=int(num[0])
x=int(num[1])
y=int(num[2])
for i in range(1,n+1):
	if (i%x==0)or(i%y==0):
		count += 1
 
print(count)