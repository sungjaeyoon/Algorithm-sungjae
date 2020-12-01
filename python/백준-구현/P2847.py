n = int(input())

arr = []

for _ in range(n):
    arr.insert(0, int(input()))

count = 0

for i in range(1, n):
    if arr[i] >= arr[i - 1]:
        num = (arr[i] - arr[i - 1] + 1)
        arr[i] -= num
        count += num

print(count)
