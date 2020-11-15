t = int(input())

for _ in range(t):
    n = int(input())
    first_row = list(map(int, input().split()))
    second_row = list(map(int, input().split()))

    d = [[0 for _ in range(n + 1)] for _ in range(2)]
    d[0][1] = first_row[0]
    d[1][1] = second_row[0]

    for i in range(2, n + 1):
        d[0][i] = max(max(d[1][i - 1], d[1][i - 2]) + first_row[i - 1], d[0][i - 1])
        d[1][i] = max(max(d[0][i - 1], d[0][i - 2]) + second_row[i - 1], d[1][i - 1])

    print(max(d[0][n], d[1][n]))
