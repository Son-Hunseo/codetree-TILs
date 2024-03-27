n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

max_num = 0

def check1(i, j):
    global max_num
    dr_list = [(0, 3), (3, 2), (2, 1), (1, 0)]
    for dr1, dr2 in dr_list:
        ni1 = i + di[dr1]
        nj1 = j + dj[dr1]
        ni2 = i + di[dr2]
        nj2 = j + dj[dr2]
        if ni1 < 0 or ni1 > n-1 or nj1 < 0 or nj1 > m-1 or ni2 < 0 or ni2 > n-1 or nj2 < 0 or nj2 > m-1:
            continue
        else:
            max_num = max(max_num, graph[i][j] + graph[ni1][nj1] + graph[ni2][nj2])
    return

def check2(i, j):
    global max_num
    for dr in range(4):
        ni1 = i + di[dr]
        nj1 = j + dj[dr]
        ni2 = i + (di[dr]*2)
        nj2 = j + (dj[dr]*2)
        if ni1 < 0 or ni1 > n-1 or nj1 < 0 or nj1 > m-1 or ni2 < 0 or ni2 > n-1 or nj2 < 0 or nj2 > m-1:
            continue
        else:
            max_num = max(max_num, graph[i][j] + graph[ni1][nj1] + graph[ni2][nj2])
    return

for i in range(n):
    for j in range(m):
        check1(i, j)
        check2(i, j)

print(max_num)