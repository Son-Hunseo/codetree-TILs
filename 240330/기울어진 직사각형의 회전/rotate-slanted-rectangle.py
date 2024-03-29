n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

i, j, m1, m2, m3, m4, dr = map(int, input().split())
i, j = i-1, j-1

di = [-1, -1, 1, 1]
dj = [1, -1, -1, 1]

data = []
candi = []

def check(i, j, m1, m2, m3, m4):
    for _ in range(m1):
        i = i + di[0]
        j = j + dj[0]
        candi.append((i, j))
        data.append(graph[i][j])
    for _ in range(m2):
        i = i + di[1]
        j = j + dj[1]
        candi.append((i, j))
        data.append(graph[i][j])
    for _ in range(m3):
        i = i + di[2]
        j = j + dj[2]
        candi.append((i, j))
        data.append(graph[i][j])
    for _ in range(m4):
        i = i + di[3]
        j = j + dj[3]
        candi.append((i, j))
        data.append(graph[i][j])

check(i, j, m1, m2, m3, m4)
data = [data[-1]] + data[:m1+m2+m3+m4-1]
candi = [candi[-1]] + candi[:m1+m2+m3+m4-1]

if dr == 0:
    data = [data[-1]] + data[:m1+m2+m3+m4-1]
else:
    data = data[1:] + [data[0]]

cnt = 0
for i, j in candi:
    graph[i][j] = data[cnt]
    cnt += 1

for row in graph:
    print(*row)