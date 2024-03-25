n, m = map(int, input().split())

mapping = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

graph = [[0 for _ in range(m)] for _ in range(n)]

dr = 3
i, j = 0, 0
cnt = 0

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

graph[i][j] = 1

while cnt != (n*m-1):
    ni = i + di[dr]
    nj = j + dj[dr]
    if ni < 0 or ni > n-1 or nj < 0 or nj > m-1 or graph[ni][nj] != 0:
        dr = (dr+3)%4
    else:
        cnt += 1
        graph[ni][nj] = graph[i][j] + 1
        i, j = ni, nj

for i in range(n):
    for j in range(m):
        graph[i][j] = mapping[(graph[i][j]-1)%26]

for row in graph:
    print(*row)