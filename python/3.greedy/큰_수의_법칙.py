""" Input
5 8 3
2 4 5 4 6
"""
N, M, K = map(int, input().split())
# M 더할 횟수
# K 연속 가능 수
# N 항 개수

data = list(map(int, input().split()))

data.sort()

first = data[N - 1]
second = data[N - 2]

# print(data, first, second)  # [2, 4, 4, 5, 6] 6 5

# K+1 개로 M 을 나누고 몫 만큼(first*K+second), 나머지 만큼 first 를더함

result = int(M/(K+1)) * (first * K + second)
result += (M % (K+1)) * first

print(result)
