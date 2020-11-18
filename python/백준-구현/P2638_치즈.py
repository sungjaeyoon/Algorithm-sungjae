from collections import deque

n, m = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 공기 층을 다 2로 만듬
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            arr[i][j] = 2

# 외벽 공기는 BFS 로 모두 0으로함
queue = deque()
queue.append([0, 0])
arr[0][0] = 0

while queue:
    p = queue.popleft()
    for i in range(4):
        nx = p[0] + dx[i]
        ny = p[1] + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 2:
                arr[nx][ny] = 0
                queue.append([nx, ny])


def is_disappear(x, y):
    global arr
    air_count = 0

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if arr[nx][ny] == 0:
            air_count += 1

    if air_count > 1:
        return True
    else:
        return False


time = 0

while True:
    # for i in range(len(arr)):
    #     print(arr[i])
    #
    # print('\n')
    remain_count = 0

    # 사라질 예정인 치즈 목록
    disappear_cheeze = []

    # 사라질 치즈 탐색
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if arr[i][j] == 1:
                remain_count += 1
                if is_disappear(i, j):
                    disappear_cheeze.append([i, j])

    # 치즈가 모두 녹은 경우
    if remain_count == 0:
        break

    time += 1

    # 치즈 제거
    for cheeze in disappear_cheeze:
        arr[cheeze[0]][cheeze[1]] = 0
        for i in range(4):
            nx = cheeze[0] + dx[i]
            ny = cheeze[1] + dy[i]
            # 공기벽이 뚫린 경우
            if arr[nx][ny] == 2:
                queue2 = deque()
                queue2.append([nx, ny])
                arr[nx][ny] = 0
                while queue2:
                    p2 = queue2.popleft()
                    for j in range(4):
                        n2x = p2[0] + dx[j]
                        n2y = p2[1] + dy[j]
                        if arr[n2x][n2y] == 2:
                            arr[n2x][n2y] = 0
                            queue2.append([n2x, n2y])


print(time)
