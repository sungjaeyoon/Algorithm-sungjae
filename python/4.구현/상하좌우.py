"""
5
R R R U D D
"""
n = int(input())
plans = list(input().split())

move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

x, y = 1, 1

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if 1 <= nx <= n and 1 <= ny <= n:
        x = nx
        y = ny

print(x, y)
