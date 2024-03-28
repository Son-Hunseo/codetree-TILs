n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

di = [-1, -1, 1, 1]
dj = [1, -1, -1, 1]

def check(i, j):
    cnt = [0, 0, 0, 0]
    result = 0
    for dr in range(4):
        while True:
            ni = i + di[dr]
            nj = j + dj[dr]
            if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
                break
            else:
                cnt[dr] += 1
                result += graph[ni][nj]
                i, j = ni, nj
    if min(cnt) < 1:
        return 0
    else:
        return result

max_result = 0
for i in range(n):
    for j in range(n):
        max_result = max(max_result, check(i, j))

print(max_result)