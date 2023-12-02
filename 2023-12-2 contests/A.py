m, d = map(int, input().split())
year, month, day = map(int, input().split())
# print(m, d, year, month, day)
ans_y = year
ans_m = month
ans_d = day + 1

if ans_d >= d:
    ans_d -= d
    ans_m += 1
    if ans_m >= m:
        ans_m -= m
        ans_y += 1

print (ans_y, ans_m, ans_d)