n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def ball_input(idx, dr):
    # 초기 진입 위치
    if dr == 0:
        cur_i = 0
        cur_j = idx
    elif dr == 1:
        cur_i = idx
        cur_j = 0
    elif dr == 2:
        cur_i = n-1
        cur_j = idx
    else:
        cur_i = idx
        cur_j = n-1
    
    # 들어간 자리에 바로 바가 있을 경우
    if graph[cur_i][cur_j] == 1:
        if dr == 0:
            dr = 1
        elif dr == 1:
            dr = 0
        elif dr == 2:
            dr = 3
        else:
            dr = 2
    elif graph[cur_i][cur_j] == 2:
        if dr == 0:
            dr = 3
        elif dr == 1:
            dr = 2
        elif dr == 2:
            dr = 1
        else:
            dr = 0
    return cur_i, cur_j, dr
    
def dfs(cur_i, cur_j, dr, time):
    ni = cur_i + di[dr]
    nj = cur_j + dj[dr]
    if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
        return time+1
    
    if graph[ni][nj] == 2:
        if dr == 0:
            dr = 1
        elif dr == 1:
            dr = 0
        elif dr == 2:
            dr = 3
        else:
            dr = 2
    elif graph[ni][nj] == 1:
        if dr == 0:
            dr = 3
        elif dr == 1:
            dr = 2
        elif dr == 2:
            dr = 1
        else:
            dr = 0
    return dfs(ni, nj, dr, time+1)

result = []
for i in range(n):
    for dr in range(4):
        cur_i, cur_j, dr = ball_input(i, dr)
        num = dfs(cur_i, cur_j, dr, 1)
        result.append(num)

print(max(result))