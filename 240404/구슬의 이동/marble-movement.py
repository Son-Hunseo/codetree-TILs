n, m, t, k = map(int, input().split())

mapping = {
    "U": 0,
    "L": 1,
    "D": 2,
    "R": 3
}

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

graph = [[0 for _ in range(n)] for _ in range(n)]
data = []

for i in range(1, m+1):
    r, c, dr, v = map(str, input().split())
    r, c, v = int(r)-1, int(c)-1, int(v)
    dr = mapping[dr]
    # i는 구슬 번호
    data.append([r, c, dr, v, i])
    graph[r][c] += 1

def change_dr(dr):
    if dr == 0:
        return 2
    elif dr == 1:
        return 3
    elif dr == 2:
        return 0
    else:
        return 1

for _ in range(t):
    ndata = []
    for con in data:
        r, c, dr, speed, num = con[0], con[1], con[2], con[3], con[4]
        for _ in range(speed):
            nr = r + di[dr]
            nc = c + dj[dr]
            if nr < 0 or nr > n-1 or nc < 0 or nc > n-1:
                dr = change_dr(dr)
                nr = r + di[dr]
                nc = c + dj[dr]
            graph[nr][nc] += 1
            graph[r][c] -= 1
            r, c = nr, nc
        ndata.append([r, c, dr, speed, num])

    # k개 이상 겹치는 부분이 있는 경우
    check = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k:
                check.append([i, j])
    
    if check:
        ndata.sort(key=lambda x: (x[3], x[4]))
        for con in check:
            cnt = graph[con[0]][con[1]] - k
            nndata = []
            for i in range(len(ndata)):
                if con[0] == ndata[i][0] and con[1] == ndata[i][1]:
                    if cnt != 0:
                        cnt -= 1
                    else:
                        nndata.append(ndata[i])
                else:
                    nndata.append(ndata[i])
            graph[con[0]][con[1]] = k
            ndata = nndata[:]
    data = ndata[:]

for row in graph:
    print(*row)