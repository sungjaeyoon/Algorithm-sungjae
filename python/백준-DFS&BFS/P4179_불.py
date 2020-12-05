n, m = map(int, input().split())

arr = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
min_len = 1001
start_x = 0
start_y = 0

for i in range(n):
    line = []
    input_line = input()
    for j in range(m):
        if input_line[j] == '#':
            line.append(0)
        elif input_line[j] == '.':
            line.append(1)
        elif input_line[j] == 'F':
            line.append(-1)
        elif input_line[j] == 'J':
            line.append(1)
            start_x = i
            start_y = j

    arr.append(line)


def move(x, y, length):

    for ar in arr:
        print(ar)
    print('--------')

    # 끝에 도착
    if x == 0 or y == 0 or x == n - 1 or y == m - 1:
        global min_len
        min_len = min(min_len, length)
        return

    fires = []
    # 불 체크
    for f_i in range(n):
        for f_j in range(m):
            # 불인 경우
            if arr[f_i][f_j] == -1:
                # 4방향
                for k in range(4):
                    fn_x = f_i + dx[k]
                    fn_y = f_j + dy[k]
                    # 배열 범위 체크
                    if 0 <= fn_x < n and 0 <= fn_y < m:
                        # 지나갈수 있는 공간
                        if arr[fn_x][fn_y] == 1:
                            fires.append([fn_x, fn_y])

    # 불 퍼트림
    for fire in fires:
        arr[fire[0]][fire[1]] = -1

    # 갈수 있는 곳으로 move
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 1:
                move(nx, ny, length+1)

    # 불 제거
    for fire in fires:
        arr[fire[0]][fire[1]] = 1


move(start_x, start_y, 0)

# 출력
if min_len == 1001:
    print('IMPOSSIBLE')
else:
    print(min_len+1)
