t = int(input())

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

mapping = {
    "U": 0,
    "L": 1,
    "D": 2,
    "R": 3
}

for _ in range(t):
    n, m = map(int, input().split())
    graph = [[0 for _ in range(n)] for _ in range(n)]
    data = []
    for _ in range(m):
        r, c, dr = map(str, input().split())
        # 인덱스화
        r, c = int(r)-1, int(c)-1
        dr = mapping[dr]
        data.append((r, c, dr))
    for r, c, _ in data:
        graph[r][c] += 1

    ndata = []
    for _ in range(2*n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > 1:
                    graph[i][j] = 0
                    for con in data:
                        if con[0] == i and con [1] == j:
                            data.remove(con)

        for r, c, dr in data:
            ni = r + di[dr]
            nj = c + dj[dr]
            if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
                ni = r
                nj = c
                dr = (dr+2)%4
                ndata.append((ni, nj, dr))
                continue
            graph[ni][nj] += 1
            graph[r][c] -= 1
            ndata.append((ni, nj, dr))
        data = ndata[:]
        ndata = []

    result = 0
    for row in graph:
        result += sum(row)

    print(result)