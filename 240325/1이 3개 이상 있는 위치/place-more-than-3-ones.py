n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def check(i, j):
    cnt = 0
    for dr in range(4):
        ni = i + di[dr]
        nj = j + dj[dr]
        if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
            continue
        if graph[ni][nj] == 1:
            cnt += 1
    if cnt >= 3:
        return True
    else:
        return False

result = 0
for i in range(n):
    for j in range(n):
        if check(i, j) == True:
            result += 1
 
print(result)