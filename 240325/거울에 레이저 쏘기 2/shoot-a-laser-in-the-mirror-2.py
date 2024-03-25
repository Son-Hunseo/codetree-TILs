n = int(input())

graph = []
for _ in range(n):
    graph.append(list(input()))

target = int(input())

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

if target % n != 0:
    if target // n == 0:
        dr = 2
        cur_i = 0
        cur_j = target % n - 1
    elif target // n == 1:
        dr = 1
        cur_i = target % n - 1
        cur_j = n-1
    elif target // n == 2:
        dr = 0
        cur_i = n-1
        cur_j = n - (target % n)
    else:
        dr = 3
        cur_i = n - (target % n)
        cur_j = 0

else:
    if target // n == 1:
        dr = 2
        cur_i = 0
        cur_j = n-1
    elif target // n == 2:
        dr = 1
        cur_i = n-1
        cur_j = n-1
    elif target // n == 3:
        dr = 0
        cur_i = n-1
        cur_j = 0
    else:
        dr = 3
        cur_i = 0
        cur_j = 0

cnt = 0
while True:
    if cur_i < 0 or cur_i > n-1 or cur_j < 0 or cur_j > n-1:
        break
    cnt += 1
    if graph[cur_i][cur_j] == "/":
        if dr == 2:
            dr = 1
        elif dr == 3:
            dr = 0
        elif dr == 0:
            dr = 3
        else:
            dr = 2
    else:
        if dr == 2:
            dr = 3
        elif dr == 3:
            dr = 2
        elif dr == 1:
            dr = 0
        else:
            dr = 1
    cur_i = cur_i + di[dr]
    cur_j = cur_j + dj[dr]

print(cnt)