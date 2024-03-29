n, m, q = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def right_wind(row_idx):
    temp = graph[row_idx][0]
    for i in range(0, m-1):
        graph[row_idx][i] = graph[row_idx][i+1]
    graph[row_idx][m-1] = temp

def left_wind(row_idx):
    temp = graph[row_idx][m-1]
    for i in range(m-1, 0, -1):
        graph[row_idx][i] = graph[row_idx][i-1]
    graph[row_idx][0] = temp

check = [0 for _ in range(n)]

def wind_blow(row_idx, dr):
    check[row_idx] = 1
    
    if row_idx < 0 or row_idx > n-1:
        return

    if dr == "L":
        left_wind(row_idx)
    else:
        right_wind(row_idx)
    
    for i in range(m):
        if 0 < row_idx:
            if graph[row_idx][i] == graph[row_idx-1][i] and check[row_idx-1] == 0:
                if dr == "L":
                    wind_blow(row_idx-1, "R")
                else:
                    wind_blow(row_idx-1, "L")
        if row_idx < n-1:
            if graph[row_idx][i] == graph[row_idx+1][i] and check[row_idx+1] == 0:
                if dr == "L":
                    wind_blow(row_idx+1, "R")
                else:
                    wind_blow(row_idx+1, "L")

for _ in range(q):
    row_idx, dr = map(str, input().split())
    row_idx = int(row_idx)-1
    wind_blow(row_idx, dr)

for row in graph:
    print(*row)