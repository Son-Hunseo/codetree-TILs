n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def check(i, j, k, l):
    cnt = 0
    for x in range(i, i+k):
        for y in range(j, j+l):
            if x < 0 or x > n-1 or y < 0 or y > m-1:
                return False
            elif graph[x][y] <= 0:
                return False
            else:
                cnt += graph[x][y]
    return k*l

result = -1
for i in range(n):
    for j in range(m):
        for k in range(1, n-i+1):
            for l in range(1, m-j+1):
                cur = check(i, j, k, l)
                if cur != False:
                    result = max(result, cur)

print(result)