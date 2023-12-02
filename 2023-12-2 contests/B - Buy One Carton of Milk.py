def minimum_cost_dp(S, M, L, N):
    INF = float('inf')
    dp = [INF] * (N + 1)  # dp[i]: i個の卵を買うために必要な最小金額

    # ベースケース: 0個の卵を買うためには金額が0円
    dp[0] = 0

    for eggs in range(1, N + 1):
        # 6個パックを買う場合
        if eggs >= 6:
            dp[eggs] = min(dp[eggs], dp[eggs - 6] + S)
        # 8個パックを買う場合
        if eggs >= 8:
            dp[eggs] = min(dp[eggs], dp[eggs - 8] + M)
        # 12個パックを買う場合
        if eggs >= 12:
            dp[eggs] = min(dp[eggs], dp[eggs - 12] + L)

    return dp[N] if dp[N] != INF else -1  # N個の卵を買うことができない場合は -1 を返す

def minimum_cost(S, M, L, N):
    min_cost = float('inf')  # 初期値を無限大に設定

    for s_count in range(N // 6 + 1):  # 6個パックの購入数
        for m_count in range(N // 8 + 1):  # 8個パックの購入数
            for l_count in range(N // 12 + 1):  # 12個パックの購入数
                total_eggs = s_count * 6 + m_count * 8 + l_count * 12
                total_cost = s_count * S + m_count * M + l_count * L

                if total_eggs >= N:
                    min_cost = min(min_cost, total_cost)

    return min_cost

n, s, m, l = map(int, input().split())
# print (n, s, m, l)

result = minimum_cost_dp(s, m, l, n)
# result = minimum_cost(s, m, l, n)
print (result)