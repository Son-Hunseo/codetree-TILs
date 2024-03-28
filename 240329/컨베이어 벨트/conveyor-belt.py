n, t = map(int, input().split())

graph = list(map(int, input().split()))
graph += list(map(int, input().split()))

def moving():
    temp = graph[2*n-1]
    for i in range(len(graph)-1, 0, -1):
        graph[i] = graph[i-1]
    graph[0] = temp

for _ in range(t):
    moving()

for i in range(n):
    if i != n-1:
        print(graph[i], end=" ")
    else:
        print(graph[i])

for i in range(n, 2*n):
    print(graph[i], end=" ")