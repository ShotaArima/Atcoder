n=int(input()) #nの読み込み

while(n%2==0):
    n/=2
# print(f"n={n}")
while(n%3==0):
    n/=3
# print(f"n={n}")
if n==1:
    print("Yes")
else:
    print("No")