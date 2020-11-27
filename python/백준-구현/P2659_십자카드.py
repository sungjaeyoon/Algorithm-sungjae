a, b, c, d = input().split()

min_number = min(min(int(a + b + c + d), int(b + c + d + a)), min(int(c + d + a + b), int(d + a + b + c)))

count = 0


def make_number(p1, p2, p3, p4):
    return 1000 * int(p1) + 100 * int(p2) + 10 * int(p3) + int(p4)


arr = set()

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for h in range(1, 10):
                num = min(min(make_number(i, j, k, h), make_number(j, k, h, i)),
                          min(make_number(k, h, i, j), make_number(h, i, j, k)))
                if num < min_number:
                    arr.add(num)


print(len(arr)+1)
