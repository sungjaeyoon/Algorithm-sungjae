n, m = map(int, input().split())

arr = []
for _ in range(n):
    line = []
    line_str = input()
    for i in range(m):
        line.append(int(line_str[i]))
    arr.append(line)

max_length = 0

for i in range(n):
    for j in range(m):
        cur_length = 0
        temp = arr[i][j]
        for k in range(0, min(n - i, m - j)):
            if arr[i][j + k] == temp and arr[i + k][j] == temp and arr[i + k][j + k] == temp:
                cur_length = k

        max_length = max(max_length, cur_length)

print((max_length+1)**2)
