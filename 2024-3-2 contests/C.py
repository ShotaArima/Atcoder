n = int(input())

result = n ** (1/3)

def is_palindrome(tmp):
    # 文字列を逆順にして比較
    reversed_tmp = tmp[::-1]
    return tmp == reversed_tmp

# 回文かの判定
for result in range(int(result), 0, -1):
    result_3 = result ** 3
    tmp = str(result_3)
    if is_palindrome(tmp):
        print(result_3)
        break

