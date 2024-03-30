n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def bomb(i, j):
    cnt = graph[i][j]
    graph[i][j] = 0
    for dr in range(4):
        for w in range(1, cnt):
            ni = i + di[dr]*w
            nj = j + dj[dr]*w
            if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
                continue
            graph[ni][nj] = 0

def fall_down():
    for j in range(n):
        temp = [[0 for _ in range(n)] for _ in range(n)]
        temp_end_idx = n-1
        for i in range(n-1, -1, -1):
            if graph[i][j] != 0:
                temp[temp_end_idx][j] = graph[i][j]
                temp_end_idx -= 1
        for i in range(n-1, -1, -1):
            if temp_end_idx < i < n:
                graph[i][j] = temp[i][j]
            else:
                graph[i][j] = 0

target_i, target_j = map(int, input().split())
target_i, target_j = target_i-1, target_j-1

bomb(target_i, target_j)
fall_down()

for row in graph:
    print(*row)