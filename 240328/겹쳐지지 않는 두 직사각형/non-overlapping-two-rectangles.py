n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def count_sum(i, j, h, w):
    cnt = 0
    for x in range(i, i+h):
        for y in range(j, j+w):
            if x < 0 or x > n-1 or y < 0 or y > m-1:
                return False
            cnt += graph[x][y]
    return cnt

candi = []
for i in range(n):
    for j in range(m):
        for h in range(1, n+1):
            for w in range(1, m+1):
                if h == n and w == m:
                    continue
                if count_sum(i, j, h, w) != False:
                    candi.append((i, j, h, w))

def check(data1, data2):
    i1, j1, h1, w1 = data1
    i2, j2, h2, w2 = data2
    graph2 = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(i1, i1+h1):
        for j in range(j1, j1+w1):
            graph2[i][j] += 1
    for i in range(i2, i2+h2):
        for j in range(j2, j2+w2):
            graph2[i][j] += 1
    for row in graph2:
        if 2 in row:
            return False
    return True

result = -99999999
for i in range(len(candi)):
    for j in range(i+1, len(candi)):
        if check(candi[i], candi[j]) == True:
            i1, j1, h1, w1 = candi[i]
            i2, j2, h2, w2 = candi[j]
            sqr_sum = count_sum(i1, j1, h1, w1) + count_sum(i2, j2, h2, w2)
            result = max(result, sqr_sum)

print(result)