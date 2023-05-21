s=input()
t=input()
copy_t=t
out=[]

for i in range(len(s)):
    for j in range(len(t)-1):
        if s[i]==copy_t[j]:
            out.append(t[j])
            # copy_t = t[:j] + "#" + t[j+1:]
            copy_t = copy_t[:j] + "#" + copy_t[j+1:]
new_s = "".join(out)
print(f"s={s},new_s={new_s}")
            
if s==new_s:
    print("Yes")
else:
    print("No")

