def is_palindrome(n):
    # 数字を文字列に変換し、逆順と比較して回文かどうかを判定
    return str(n) == str(n)[::-1]

n = int(input())

# N以下の正整数であって回文立方数であるものの最大値を求める
result = 0
for x in range(int(n ** (1/3)), 0, -1):
    cube = x ** 3
    if cube <= n and is_palindrome(cube):
        result = max(result, cube)

print(result)
