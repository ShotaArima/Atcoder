count=0

n,s=map(int,input().split())
print(f"s={s}, num={n}")

for i in range(1,n+1):
    for j in range(1,n+1):
        if(i+j>s):
            break
        print(f"{i}+{j}={i+j}")
        count+=1
print(count)