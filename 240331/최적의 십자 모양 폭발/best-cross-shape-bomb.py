n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def bomb(bomb_i, bomb_j, graph):
    # 폭탄 터짐
    value = graph[bomb_i][bomb_j]
    graph[bomb_i][bomb_j] = 0
    for cnt in range(1, value):
        for dr in range(4):
            ni = bomb_i + di[dr]*cnt
            nj = bomb_j + dj[dr]*cnt
            if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
                continue
            graph[ni][nj] = 0
    # 중력 작용
    for j in range(n):
        temp = []
        for i in range(n-1, -1, -1):
            if graph[i][j] != 0:
                temp.append(graph[i][j])
        len_temp = len(temp)
        while len_temp < n:
            temp.append(0)
            len_temp += 1
        for i in range(n-1, -1, -1):
            graph[i][j] = temp[n-i-1]
    return graph

def check(graph):
    cnt = 0
    # 가로로 인접
    for i in range(n):
        bf = -1
        for j in range(n):
            if graph[i][j] == 0:
                bf = 0
            else:
                if graph[i][j] == bf:
                    cnt += 1
                else:
                    bf = graph[i][j]
    # 세로로 인접
    for j in range(n):
        bf = -1
        for i in range(n):
            if graph[i][j] == 0:
                bf = 0
            else:
                if graph[i][j] == bf:
                    cnt += 1
                else:
                    bf = graph[i][j]
    return cnt

result = 0
for i in range(n):
    for j in range(n):
        ngraph = [row[:] for row in graph]
        num = check(bomb(i, j, ngraph))
        if num > result:
            result = num

print(result)