n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def bomb(j):
    # find target
    target_i = -1
    target_v = -1
    for i in range(n):
        if graph[i][j] != 0:
            target_v = graph[i][j]
            target_i = i
            break

    graph[target_i][j] = 0
    for dr in range(4):
        for cnt in range(1, target_v):
            ni = target_i + di[dr]*cnt
            nj = j + dj[dr]*cnt
            if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
                continue
            graph[ni][nj] = 0

def fall_down():
    for j in range(n):
        temp = []
        for i in range(n-1, -1, -1):
            if graph[i][j] != 0:
                temp.append(graph[i][j])
        cnt = len(temp)
        while cnt < n:
            temp.append(0)
            cnt += 1
        for i in range(n-1, -1, -1):
            graph[i][j] = temp[n-i-1]

for _ in range(m):
    col = int(input())
    col -= 1
    bomb(col)
    fall_down()

for row in graph:
    print(*row)