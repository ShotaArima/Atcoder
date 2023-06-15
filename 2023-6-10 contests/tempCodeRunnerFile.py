h,w=map(int,input().split())
table=[]
for _ in range(h):
    x=input()
    row=list(x)
    table.append(row)

# for row in table:
#     print(row)
quadrangle=[]
for i in range(h):
    for j in range(w):
        if table[i][j]=="#":
            quadrangle.append([i, j])
            
print(quadrangle)

# 行と列の最大値を求める
max_row = max(coord[0] for coord in quadrangle)
max_col = max(coord[1] for coord in quadrangle)

# サイズを特定する
size = (max_row + 1, max_col + 1)

print(max_row,max_col)