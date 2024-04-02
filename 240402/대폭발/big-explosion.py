n, m, r, c = map(int, input().split())
r, c = r-1, c-1

graph = [[0 for _ in range(n)] for _ in range(n)]

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

q = []

def bomb(r, c, time):
    global graph
    if time == m+1:
        return
    
    graph[r][c] = 1
    q = []
    for dr in range(4):
        nr = r + di[dr]*(2**(time-1))
        nc = c + dj[dr]*(2**(time-1))
        if nr < 0 or nr > n-1 or nc < 0 or nc > n-1:
            continue
        q.append((nr, nc, time+1))
        graph[nr][nc] = 1
    
    for i in range(len(q)):
        nr, nc, nt = q[i]
        bomb(nr, nc, nt)
    bomb(r, c, time+1)

bomb(r, c, 1)

result = 0
for row in graph:
    result += sum(row)

print(result)