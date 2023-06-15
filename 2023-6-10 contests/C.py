h,w=map(int,input().split())
table=[]
for _ in range(h):
    x=input()
    row=list(x)
    table.append(row)

# for row in table:
#     print(row)
quadrangle=[]
ans=[]
memory=[]
for i in range(h):
    for j in range(w):
        if table[i][j]=="#":
            quadrangle.append([i, j])
    ans.append(len(quadrangle))
    memory.append(quadrangle)
    quadrangle=[]
    
# print(quadrangle)
print(ans)

non_zero_values = set(filter(lambda x: x != 0, ans))

if len(non_zero_values) > 1:
    for i, num in enumerate(ans):
        if num != 0 and num not in non_zero_values:
            print(i)


        