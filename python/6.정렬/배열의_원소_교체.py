"""
5 3
1 2 5 4 3
5 5 6 6 5
"""

n, k = map(int, input().split())

arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

arrA.sort()
arrB.sort(reverse=True)

for i in range(k):
    if arrB[i] > arrA[i]:
        arrA[i], arrB[i] = arrB[i], arrA[i]
    else:
        break

print(sum(arrA))
