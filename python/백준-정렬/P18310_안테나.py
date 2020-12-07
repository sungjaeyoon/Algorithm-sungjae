import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

t = (len(arr)-1) // 2

print(arr[t])