"""
5
8 3 7 9 2
3
5 7 9
"""
n = int(input())
arr = list(map(int, input().split()))

m = int(input())
request_numbers = list(map(int, input().split()))

arr.sort()


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


for i in request_numbers:
    result = binary_search(arr, i, 0, n - 1)
    if result is not None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
