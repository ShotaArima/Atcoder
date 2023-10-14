n=int(input()) #nの読み込み
a = [int(x) for x in input().split()] #配列aの読込
judge=True

for i in range(len(a)-1):
    if a[i]!=a[i+1]:
        judge=False
        print("No")
        break
if judge:
    print("Yes")