n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def mining(row, col, m, k):
    gold_num = 0
    cnt = 0
    for i in range(n):
        for j in range(n):
            if abs(row - i) + abs(col - j) <= k:
                cnt += graph[i][j]
    if m*cnt >= k**2 + (k+1)**2:
        return cnt
    else:
        return 0

result = 0
for i in range(n):
    for j in range(n):
        for k in range(2*n-1):
            result = max(result, mining(i, j, m, k))

print(result)