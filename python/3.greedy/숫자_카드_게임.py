"""
3 3
3 1 2
4 1 4
2 2 2
"""

M, N = map(int, input().split())
data = []

for i in range(N):
    data.append(list(map(int, input().split())))

result = 0

for lis in data:
    min_value = min(lis)
    result = max(min_value, result)

print(result)