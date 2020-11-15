"""
4 6
19 15 10 17
"""

import sys

n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(arr)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in arr:
        if i > mid:
            total += i - mid

    if total > m:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(mid)
