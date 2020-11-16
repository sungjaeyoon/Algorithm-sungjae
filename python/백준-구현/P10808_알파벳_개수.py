s = input()

arr = [0] * 26
for i in range(len(s)):
    arr[ord(s[i]) - 97] += 1

for i in arr:
    print(i, end=' ')
