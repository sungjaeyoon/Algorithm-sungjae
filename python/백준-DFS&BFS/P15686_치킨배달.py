import sys

sys.setrecursionlimit(10000)

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

chickens = []
houses = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chickens.append([i, j])
        elif arr[i][j] == 1:
            houses.append([i, j])

visited = [False] * len(chickens)

min_result = 1000001


def select_rest(count, cur):
    visited[cur] = True
    if count == m:

        result = 0
        # 가장 가까운 치킨집 거리만 더거리 계산
        for house in houses:
            min_length = 10000001
            for d in range(len(chickens)):
                if visited[d]:
                    chicken = chickens[d]
                    length = 0
                    length += abs(house[0] - chicken[0])
                    length += abs(house[1] - chicken[1])
                    min_length = min(min_length, length)

            result += min_length

        global min_result
        min_result = min(min_result, result)
        visited[cur] = False
        return

    for k in range(cur + 1, len(chickens)):
        select_rest(count + 1, k)

    visited[cur] = False


for i in range(len(chickens)):
    select_rest(1, i)

print(min_result)
