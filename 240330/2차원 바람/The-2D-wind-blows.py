n, m, q = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def wind_blow(r1, c1, r2, c2):
    # 좌측 상단
    temp1 = graph[r1][c1]
    # 우측 상단
    temp2 = graph[r1][c2]
    # 우측 하단
    temp3 = graph[r2][c2]
    # 좌측 하단
    temp4 = graph[r2][c1]

    # 위
    for i in range(c2, c1+1, -1):
        graph[r1][i] = graph[r1][i-1]
    # 오른쪽 
    for i in range(r2, r1+1, -1):
        graph[i][c2] = graph[i-1][c2]
    # 아래
    for i in range(c1, c2-1):
        graph[r2][i] = graph[r2][i+1]
    # 왼쪽
    for i in range(r1, r2-1):
        graph[i][c1] = graph[i+1][c1]
    # 정산
    graph[r1][c1+1] = temp1
    graph[r1+1][c2] = temp2
    graph[r2][c2-1] = temp3
    graph[r2-1][c1] = temp4

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def cal_mean(r1, c1, r2, c2):
    fake_graph = [row[:] for row in graph]
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            cnt = 1
            num_sum = fake_graph[i][j]
            for dr in range(4):
                ni = i + di[dr]
                nj = j + dj[dr]
                if ni < 0 or ni > n-1 or nj < 0 or nj > m-1:
                    continue
                cnt += 1
                num_sum += fake_graph[ni][nj]
            graph[i][j] = num_sum // cnt


for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1
    wind_blow(r1, c1, r2, c2)
    cal_mean(r1, c1, r2, c2)

for row in graph:
    print(*row)