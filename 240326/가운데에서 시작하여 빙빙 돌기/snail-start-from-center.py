n = int(input())

graph = [[0 for _ in range(n)] for _ in range(n)]

i, j = (n-1)//2, (n-1)//2
dr = 3
cnt = 0

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

graph[i][j] = 1
j += 1
graph[i][j] = 2

while cnt != n*n-2:
    li = i + di[(dr+1)%4]
    lj = j + dj[(dr+1)%4]
    if graph[li][lj] == 0:
        dr = (dr+1)%4
    else:
        cnt += 1
        ni = i + di[dr]
        nj = j + dj[dr]
        graph[ni][nj] = graph[i][j] + 1
        i, j = ni, nj

for row in graph:
    print(*row)