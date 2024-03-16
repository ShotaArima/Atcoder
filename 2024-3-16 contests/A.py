s = input()
# print(s)

reversed_s = s[::-1]
fixed_s = ""
for char in reversed_s:
    if char == ">":
        fixed_s += "<"
    elif char == "<":
        fixed_s += ">"
    else:
        fixed_s += char
# print(fixed_s)

if fixed_s == s:
    print("Yes")
else:
    print("No")