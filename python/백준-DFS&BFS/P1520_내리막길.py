import sys

sys.setrecursionlimit(10000)
n, m = map(int, input().split())

arr = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [[-1 for _ in range(m)] for _ in range(n)]


def dfs(x, y):
    global dp
    if x == n - 1 and y == m - 1:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[x][y] > arr[nx][ny]:
                    dp[x][y] += dfs(nx, ny)

    return dp[x][y]



dfs(0, 0)
print(dp[0][0])
