n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]

for _ in range(m):
    data = [[] for _ in range(n**2)]
    for i in range(n):
        for j in range(n):
            data[graph[i][j]-1] = [i, j]
    for i in range(len(data)):
        candi = [0 for _ in range(8)]
        cur_i, cur_j = data[i][0], data[i][1]
        for dr in range(8):
            ni, nj = cur_i + di[dr], cur_j + dj[dr]
            if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
                continue
            candi[dr] = graph[ni][nj]
        dr = candi.index(max(candi))
        ni, nj = cur_i + di[dr], cur_j + dj[dr]
        graph[cur_i][cur_j], graph[ni][nj] = graph[ni][nj], graph[cur_i][cur_j]
        data[graph[cur_i][cur_j]-1], data[graph[ni][nj]-1] = data[graph[ni][nj]-1], data[graph[cur_i][cur_j]-1]
            
for row in graph:
    print(*row)