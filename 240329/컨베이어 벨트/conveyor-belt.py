n, t = map(int, input().split())

graph = []
for _ in range(2):
    graph.append(list(map(int, input().split())))

def moving():
    temp1 = graph[0][n-1]
    temp2 = graph[1][0]
    for i in range(n-1, 0, -1):
        graph[0][i] = graph[0][i-1]
    for j in range(0, n-1):
        graph[1][j] = graph[1][j+1]
    graph[0][0] = temp2
    graph[1][n-1] = temp1

for _ in range(t):
    moving()

for row in graph:
    print(*row)