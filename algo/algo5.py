sum=0
num=int(input())
nums=input().split()
for i in range(num):
	sum+=int(nums[i])
print(sum%100)