import sys

n, m = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

count_year = 0
while True:

    count_year += 1
    count_water = [[0 for _ in range(m)] for _ in range(n)]

    # 녹일 빙산 찾기
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        if arr[nx][ny] == 0:
                            count_water[i][j] += 1

    # 빙산 녹임
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                arr[i][j] -= count_water[i][j]
                if arr[i][j] < 0:
                    arr[i][j] = 0

    # 빙산 카운트
    dfs_count = 0
    visited = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0 and not visited[i][j]:
                dfs_count += 1
                # 이어진 빙산 방문 처리
                visited[i][j] = True
                queue = [[i, j]]
                while queue:
                    p = queue.pop()
                    for k in range(4):
                        nx = p[0] + dx[k]
                        ny = p[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < m:
                            if arr[nx][ny] > 0 and not visited[nx][ny]:
                                queue.append([nx, ny])
                                visited[nx][ny] = True

    # 종료 조건
    if dfs_count > 1:
        break

    # 모두 녹은 경우
    total = 0
    for i in arr:
        total += sum(i)

    if total == 0:
        print(0)
        exit()
print(count_year)
