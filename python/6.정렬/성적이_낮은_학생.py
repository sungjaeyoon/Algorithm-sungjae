"""
2
홍길동 95
이순신 77
"""
n = int(input())

arr = []

for i in range(n):
    name, score = input().split()
    arr.append((name, int(score)))


result = sorted(arr, key=lambda student: student[1])
print(result)