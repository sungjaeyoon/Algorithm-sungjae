n, m = map(int, input().split())

arr = []

for _ in range(n):
    line = []
    input_line = input()
    for i in range(m):
        line.append(input_line[i])

    arr.append(line)

print(arr)