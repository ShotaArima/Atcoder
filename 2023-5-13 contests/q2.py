num=int(input())
nums = list(map(int, input().split()))

return_num=[]

for i in range(num-1):
    return_num.append(nums[i])
    if nums[i]<nums[i+1]:
        for j in range(nums[i]+1,nums[i+1]):
            return_num.append(j)
    else:
        for j in range(nums[i]-1,nums[i+1],-1):
            return_num.append(j)
return_num.append(nums[num-1])

str_nums = ' '.join(map(str, return_num))
print(str_nums)

