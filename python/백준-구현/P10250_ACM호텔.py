t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())

    room_number = (n // h) + 1
    room_floor = n % h

    if room_floor == 0:
        room_floor = h
        room_number -= 1

    if room_number < 10:
        print(str(room_floor) + '0' + str(room_number))
    else:
        print(str(room_floor) + str(room_number))
