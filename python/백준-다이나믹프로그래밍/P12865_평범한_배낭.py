n, k = map(int, input().split())

product_list = []
dp = [0] * (k + 1)

for i in range(n):
    w, v = map(int, input().split())
    if w <= k:
        product_list.append([w, v])

for i in range(1, k + 1):
    dp[i] = dp[i-1]
    for product in product_list:
        if i == product[0]:
            dp[i] = max(dp[i], product[1])
        if i - product[0] >= 0:
            dp[i] = max(dp[i], dp[i-product[0]] + product[1])


print(dp)
