count=0
i=1
nums=input().split()
num=int(nums[0])
s=int(nums[1])
print(f"s={s}, num={num}")
while i<=num:
    j=0
    while i+j<s:
        j+=1
        # print(f"{i}+{j}={i+j}")
        count+=1
    i+=1
print(count)
