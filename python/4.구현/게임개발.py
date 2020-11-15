"""
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""
n, m = map(int, input().split())
x, y, direction = map(int, input().split())

# 0 1 2 3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

arr = []
visited = [[False for col in range(m)] for row in range(n)]

for i in range(n):
    line = list(map(int, input().split()))
    arr.append(line)


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 0
rotation_count = 0

while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if not visited[nx][ny] and arr[nx][ny] == 0:
        x = nx
        y = ny
        visited[nx][ny] = True
        rotation_count = 0
        count += 1
        continue

    rotation_count += 1

    if rotation_count == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if arr[nx][ny] == 0:
            x = nx
            y = ny
            rotation_count = 0
        else:
            break

print(count)
