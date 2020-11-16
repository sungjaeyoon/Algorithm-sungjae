"""
7
7
8
10
11
9
11
"""
n = int(input())

arr = list(map(int, input().split()))

arr_sum = [0] * n

arr_sum[0] = arr[0]
arr_sum[1] = arr[1]

if n == 2:
    print(max(arr))
    exit()

for i in range(2, n):
    arr_sum[i] = arr_sum[i - 2] + arr[i]

max_total = arr_sum[n - 1]

for i in range(1, n + 1):
    total = 0
    if i % 2 != 0:
        total = arr_sum[i - 1] + arr_sum[n - 3]
        if i >= 2:
            total -= arr_sum[i - 2]
    else:
        total = arr_sum[i - 2] + arr_sum[n - 1] - arr_sum[i - 1]

    max_total = max(max_total, total)

print(max_total)
