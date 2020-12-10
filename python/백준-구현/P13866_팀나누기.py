a, b, c, d = map(int, input().split())

min_len = abs((a + b) - (c + d))
min_len = min(min_len, abs((a + c) - (b + d)))
min_len = min(min_len, abs((a + d) - (b + c)))
min_len = min(min_len, abs((b + c) - (a + d)))
min_len = min(min_len, abs((b + d) - (a + c)))
min_len = min(min_len, abs((c + d) - (a + b)))

print(min_len)