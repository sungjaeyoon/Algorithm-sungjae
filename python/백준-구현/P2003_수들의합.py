import sys

n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

if len(arr) == 1:
    if arr[0] == m:
        print(1)
    else:
        print(0)
    exit()

arr_sum = [0] * n
arr_sum[0] = arr[0]

for i in range(1, len(arr)):
    arr_sum[i] = arr_sum[i - 1] + arr[i]

count = 0

for i in range(len(arr)):
    for j in range(i, len(arr)):
        if (arr_sum[j] - arr_sum[i] + arr[i]) == m:
            count += 1

print(count)
