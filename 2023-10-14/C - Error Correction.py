import re
# 条件2,3の関数
def check_deleted_string(string1, string2):
    if abs(len(string1) - len(string2)) != 1:
        return False

    # 文字列の差を求める
    diff = [char1 != char2 for char1, char2 in zip(string1, string2)]
    # 最初の異なる位置を見つける
    first_difference = next((i for i, is_diff in enumerate(diff) if is_diff), None)
    if first_difference is None:
        # 全ての文字が一致している場合
        return True if len(string1) > len(string2) else False
    # 差が1つで、その位置以降が一致している場合
    return all(diff[first_difference + 1:]) and len(string1) == len(string2) + 1

# 条件4の関数
def is_one_character_replaced(string1, string2):
    # 文字列の長さが異なる場合は変更されたものとみなす
    if len(string1) != len(string2):
        return False

    # 異なる文字の数をカウント
    diff_count = sum(char1 != char2 for char1, char2 in zip(string1, string2))

    # 異なる文字の数が1つの場合、かつ小文字に変更されている場合にTrueを返す
    return diff_count == 1


n, t = input().split()  # nとtを受け取る
n = int(n)  # nを整数に変換
t = str(t)
s = []  # 文字列の長さを格納する空の配列

# n個の文字列を受け取り、配列sに格納
for i in range(n):
    s.append(str(input()))

result=[]
count=0

for i in range(n):
    # 条件1
    if t==s[i]:
        count+=1
        result.append(i+1)

    # 条件2
    elif(check_deleted_string(s[i],t)==True):
        count+=1
        result.append(i+1)

    # 条件3
    elif(check_deleted_string(t,s[i])==True):
        count+=1
        result.append(i+1)

    # 条件4
    elif(is_one_character_replaced(t,s[i])==True):
        count+=1
        result.append(i+1)

result = ' '.join(map(str, result))  # 数字のリストを文字列に変換し、スペースで結合

print(count)
print(result)