n = int(input())
arr = list(map(int, input().split()))

"""
i 번째 
d[i-1] > d[i-2] + arr[i]
"""

d = [0] * 101
d[0] = arr[0]
d[1] = max(d[0], arr[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + arr[i])

print(d[n-1])