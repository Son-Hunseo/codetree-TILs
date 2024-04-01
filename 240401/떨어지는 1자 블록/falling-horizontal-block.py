n, m, k = map(int, input().split())
# 순서 k를 인덱스로 바꿈
k -= 1

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for j in range(k, k+m):
    graph[0][j] = 1

def fall_down():
    cur_row = 0
    while True:
        ni = cur_row + 1
        for j in range(k, k+m):
            if ni < 0 or ni > n-1:
                return
            if graph[ni][j] == 1:
                return
        for j in range(k, k+m):
            graph[cur_row][j] = 0
            graph[ni][j] = 1
        cur_row += 1

fall_down()

for row in graph:
    print(*row)