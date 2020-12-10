n, m = map(int, input().split())

d = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, m + 1):
    d[0][i] = 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        d[i][j] = (d[i][j - 1] + d[i - 1][j]) % 1000000000

print(d[n][m])
