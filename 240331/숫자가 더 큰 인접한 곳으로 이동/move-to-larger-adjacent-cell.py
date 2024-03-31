n, r, c = map(int, input().split())
ini_r, ini_c = r-1, c-1

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 우선순위 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def move(i, j):
    check = [0, 0, 0, 0]
    for dr in range(4):
        ni = i + di[dr]
        nj = j + dj[dr]
        if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
            continue
        if graph[ni][nj] > graph[i][j]:
            check[dr] = 1
    for idx in range(len(check)):
        if check[idx] == 1:
            return i + di[idx], j + dj[idx]
    return i, j

cur_i, cur_j = ini_r, ini_c
result = []
while True:
    result.append(graph[cur_i][cur_j])
    i, j = move(cur_i, cur_j)
    if cur_i == i and cur_j == j:
        break
    else:
        cur_i, cur_j = i, j

print(*result)