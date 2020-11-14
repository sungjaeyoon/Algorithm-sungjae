"""
3
15
27
12
"""
n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

result = sorted(arr, reverse=True)

print(result)
