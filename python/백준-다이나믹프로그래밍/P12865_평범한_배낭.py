n, k = map(int, input().split())

product = [[0, 0]]

for _ in range(n):
    product.append(list(map(int, input().split())))

dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= product[i][0]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - product[i][0]] + product[i][1])

print(dp[n][k])
