n, m, t = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

balls = []
check = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    r, c = map(int, input().split())
    r, c = r-1, c-1
    check[r][c] += 1

# 초기부터 겹치는 것 정리
for i in range(n):
    for j in range(n):
        if check[i][j] > 1:
            check[i][j] = 0

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def ball_move(r, c):
    candi = [0, 0, 0, 0]
    for dr in range(4):
        ni = r + di[dr]
        nj = c + dj[dr]
        if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
            continue
        else:
            candi[dr] = graph[ni][nj]
    if candi:
        dr = candi.index(max(candi))
        return r + di[dr], c + dj[dr]
    else:
        return r, c

for _ in range(t):
    ball_loca = []
    for i in range(n):
        for j in range(n):
            if check[i][j] == 1:
                ball_loca.append((i, j))
    for i in range(len(ball_loca)):
        cur_i, cur_j = ball_loca[i][0], ball_loca[i][1]
        ni, nj = ball_move(cur_i, cur_j)
        check[cur_i][cur_j] -= 1
        check[ni][nj] += 1
    for i in range(n):
        for j in range(n):
            if check[i][j] > 1:
                check[i][j] = 0

result = 0
for i in range(n):
    for j in range(n):
        if check[i][j] == 1:
            result += 1

print(result)