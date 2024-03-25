n, m = map(int, input().split())

graph = [[0 for _ in range(m)] for _ in range(n)]

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

dr = 2
i, j = 0, 0
graph[i][j] = 1
cnt = 0

while cnt != (n*m-1):
    ni = i + di[dr]
    nj = j + dj[dr]
    if ni < 0 or ni > n-1 or nj < 0 or nj > m-1 or graph[ni][nj] != 0:
        dr = (dr+1)%4
    else:
        cnt += 1
        graph[ni][nj] = graph[i][j] + 1
        i, j = ni, nj

for row in graph:
    print(*row)