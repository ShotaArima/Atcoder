n=list(map(int,input().split()))

ans=0
for i in range(len(n)):
    ans+=(n[i]*pow(2,i))

print(ans)