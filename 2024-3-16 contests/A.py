s = input()

# 最初の文字が < であり、最後の文字が > であることを確認
if s[0] != "<" or s[-1] != ">":
    print("No")
else:
    # 最初と最後の文字を除いた部分がすべて = であることを確認
    if all(char == "=" for char in s[1:-1]):
        print("Yes")
    else:
        print("No")
