from collections import deque
import sys

inputs = sys.stdin.readline


def bfs():
    global q, f
    while q:
        temp = deque()
        while q:
            x, y = q.popleft()
            if (x == r - 1 or y == c - 1 or x == 0 or y == 0) and s[x][y] != "F": return s[x][y] + 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and s[nx][ny] == "." and s[x][y] != "F":
                    temp.append([nx, ny])
                    s[nx][ny] = s[x][y] + 1
        q = temp
        if not q: break
        temp = deque()
        while f:
            x, y = f.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and visit[nx][ny] == 0 and s[nx][ny] != "#":
                    temp.append([nx, ny])
                    visit[nx][ny] = 1
                    s[nx][ny] = "F"
        f = temp


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
r, c = map(int, inputs().split())
s = []
q = deque()
f = deque()
visit = [[0] * c for i in range(r)]
for i in range(r):
    a = list(inputs().strip())
    s.append(a)
    for j in range(c):
        if a[j] == "J":
            q.append([i, j])
            s[i][j] = 0
        elif a[j] == "F":
            f.append([i, j])
            visit[i][j] = 1
result = bfs()

print(result if result is not None else "IMPOSSIBLE")
