n, m, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def turn():
    global graph
    graph = list(map(list, zip(*graph)))
    graph = [row[::-1] for row in graph]

def bomb(j):
    cur = -1
    candi = []
    # 폭탄 터트리기
    for i in range(n):
        if graph[i][j] == cur:
            candi.append(i)
        else:
            if len(candi) >= m:
                for r in candi:
                    graph[r][j] = 0
            cur = graph[i][j]
            candi = []
            candi.append(i)
    # 마지막에 연속된 폭탄 터트리기
    if len(candi) >= m:
        for r in candi:
            graph[r][j] = 0
        candi = []

def check(j):
    global graph
    cur = -1
    cnt = 0
    candi = []
    for i in range(n):
        if graph[i][j] != 0:
            if graph[i][j] == cur:
                cnt += 1
            else:
                candi.append(cnt)
                cur = graph[i][j]
                cnt = 1
    candi.append(cnt)
    if max(candi) >= m:
        return True
    else:
        return False

def gravity(j):
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

for cnt in range(k+1):
    for i in range(n):
        while check(i) == True:
            bomb(i)
            gravity(i)
    if cnt != k:
        turn()
        for i in range(n):
            gravity(i)

result = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            result += 1

print(result)