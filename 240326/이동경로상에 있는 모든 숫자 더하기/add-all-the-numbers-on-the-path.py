n, t = map(int, input().split())
data = list(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

i, j = (n-1)//2, (n-1)//2
dr = 0

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

cnt = graph[i][j]

for k in range(len(data)):
    if data[k] == "L":
        dr = (dr+1)%4
    elif data[k] == "R":
        dr = (dr+3)%4
    else:
        ni = i + di[dr]
        nj = j + dj[dr]
        if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
            continue
        else:
            cnt += graph[ni][nj]
            i, j = ni, nj

print(cnt)