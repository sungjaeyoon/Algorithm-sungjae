n = int(input())
arr = list(map(int, input().split()))

d = [1] * (n + 1)

for i in range(1, n):
    max_index = 0
    for j in range(0, i):
        if arr[j] < arr[i]:
            max_index = max(max_index, d[j] + 1)

    d[i] = max(max_index, d[i])

print(max(d))
