from _collections import deque


def is_empty(q):
    if len(q) == 0:
        return True
    else:
        return False


while True:
    line = input()

    if line == '.':
        break

    queue = deque()

    isRight = True

    for i in range(len(line)):
        if line[i] == "(" or line[i] == "[":
            queue.append(line[i])
        elif line[i] == ")":
            if is_empty(queue):
                isRight = False
                break
            if queue.pop() != "(":
                isRight = False
                break
        elif line[i] == "]":
            if is_empty(queue):
                isRight = False
                break
            if queue.pop() != "[":
                isRight = False
                break

    if not is_empty(queue):
        isRight = False

    if isRight:
        print("yes")
    else:
        print("no")
