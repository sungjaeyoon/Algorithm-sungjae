n, k = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))

d = [10001] * (k + 1)
d[0] = 0

for i in range(n):
    for j in range(arr[i], k + 1):
        if d[j - arr[i]] != 10001:
            d[j] = min(d[j], d[j - arr[i]] + 1)

if d[k] == 10001:
    print(-1)
else:
    print(d[k])
