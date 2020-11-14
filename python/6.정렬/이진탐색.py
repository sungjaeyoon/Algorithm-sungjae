def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) / 2

    if array[mid] == target:
        return mid

    elif array[mid] > target:
        binary_search(array, target, start, mid - 1)

    else:
        binary_search(array, target, mid + 1, end)


def binary_search_while(array, target, start, end):
    while start <= end:
        mid = (start + end) / 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
