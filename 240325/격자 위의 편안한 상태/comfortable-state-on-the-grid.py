n, m = map(int, input().split())

graph = [[0 for _ in range(n)] for _ in range(n)]

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

for _ in range(m):
    i, j = map(int, input().split())
    i, j = i-1, j-1
    graph[i][j] = 1
    cnt = 0
    for dr in range(4):
        ni = i + di[dr]
        nj = j + dj[dr]
        if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
            continue
        if graph[ni][nj] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)