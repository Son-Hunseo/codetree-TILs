import copy

n, m = map(int, input().split())

i, j = 0, 0
dr = 3
graph = [[0 for _ in range(m)] for _ in range(n)]
graph[0][0] = 1

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

cnt = 0
while cnt != n*m-1:
    ni = i + di[dr]
    nj = j + dj[dr]
    if ni < 0 or ni > n-1 or nj < 0 or nj > m-1 or graph[ni][nj] != 0:
        if dr == 3:
            dr = 1
        elif dr == 1:
            dr = 2
        elif dr == 2:
            dr = 0
        else:
            dr = 3
    else:
        graph[ni][nj] = graph[i][j]+1
        cnt += 1
        i = ni
        j = nj

for row in graph:
    print(*row)