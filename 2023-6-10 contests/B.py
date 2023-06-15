char = input().split()
ans=[]
for i in range(2):
    if(char[i]=="A"):
        ans.append(0)
    elif(char[i]=="B"):
        ans.append(3)
    elif(char[i]=="C"):
        ans.append(4)
    elif(char[i]=="D"):
        ans.append(8)
    elif(char[i]=="E"):
        ans.append(9)
    elif(char[i]=="F"):
        ans.append(14)
    elif(char[i]=="G"):
        ans.append(23)
    
# print(ans)

print(abs(ans[1]-ans[0]))