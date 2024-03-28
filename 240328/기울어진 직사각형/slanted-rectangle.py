n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

di = [-1, -1, 1, 1]
dj = [1, -1, -1, 1]

def check(i, j, a, b):
    cnt = 0
    for dr in range(4):
        if dr == 0 or dr == 2:
            for _ in range(1, a+1):
                ni = i + di[dr]
                nj = j + dj[dr]
                if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
                    # 주어진 길이의 사각형이 범위를 벗어나면 그냥 무조건 0 리턴
                    return 0
                cnt += graph[ni][nj]
                i, j = ni, nj
        else:
            for _ in range(1, b+1):
                ni = i + di[dr]
                nj = j + dj[dr]
                if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
                    # 주어진 길이의 사각형이 범위를 벗어나면 그냥 무조건 0 리턴
                    return 0
                cnt += graph[ni][nj]
                i, j = ni, nj
    return cnt

result = 0
for i in range(n):
    for j in range(n):
        for x in range(1, n):
            for y in range(1, n):
                result = max(result, check(i, j, x, y))

print(result)