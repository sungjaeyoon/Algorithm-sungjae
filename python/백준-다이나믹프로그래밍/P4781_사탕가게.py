while True:
    n, m = input().split()

    n = int(n)
    m = int((float(m) * 100) + 0.5)

    if n == 0:
        break

    cal = []
    price = []
    d = [0] * (m + 1)

    for i in range(n):
        c, p = input().split()
        cal.append(int(c))
        price.append(int((float(p) * 100) + 0.5))

    for i in range(len(cal)):
        for j in range(price[i], m + 1):
            d[j] = max(d[j], d[j - price[i]] + cal[i])

    print(d[m])
