def count_ones(string):
    count = 0
    for char in string:
        if char.isdigit() and char == '1':
            count += 1
    return count

# テスト用の文字列
test_string=input()

# カウントを取得
ones_count = count_ones(test_string)

# 結果を出力
print(ones_count)