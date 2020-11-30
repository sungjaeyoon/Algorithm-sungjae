arr = list(map(int, input().split()))

while True:
    finish = True

    for i in range(4):
        if arr[i] != i + 1:
            finish = False
        if arr[i] > arr[i+1]:
            arr[i+1], arr[i] = arr[i], arr[i+1]
            for j in arr:
                print(j, end=' ')
            print('')
    if finish:
        break
