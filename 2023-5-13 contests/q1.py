num=int(input())
judge=str(input())
count_a=0
count_t=0
for i in range(num):
    if judge[i]=="A":
        count_a+=1
    else:
        count_t+=1
    
if count_a>count_t:
    print("A")
elif count_t>count_a:
    print("T")
else:
    if judge[num-1]=="A":
        print("T")
    elif judge[num-1]=="T":
        print("A")


# https://atcoder.jp/contests/abc301
# 模範解答

# N,S=int(input()),input()　nとsの入力

# 文字列メソッドcount():指定された(部分)文字列が、対象となる文字列内にいくつ出現するかを数える
# T,A=S.count("T"),S.count("A")　

# print("T" if T>A or T==A and S[-1]=="A" else "A")