n=input()
s =str(input())
char=list(s)

ans=[]
for i in range(len(char)):
    for _ in range(2):
        ans.append(char[i])
        
answer = ''.join(ans)
print(answer)
    