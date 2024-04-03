n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(list, input().split())))

for i in range(n):
    for j in range(n):
        graph[i][j][0] = int(graph[i][j][0])

move_list = list(map(int, input().split()))

di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]

for num in move_list:
    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                if num in graph[i][j]:
                    cur_i, cur_j = i, j

    candi = [0 for _ in range(8)]
    for dr in range(8):
        ni = cur_i + di[dr]
        nj = cur_j + dj[dr]
        if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
            continue
        if graph[ni][nj]:
            candi[dr] = max(graph[ni][nj])
    dr = candi.index(max(candi))
    ni = cur_i + di[dr]
    nj = cur_j + dj[dr]
    
    # 해당 위치의 리스트에서 현재 숫자의 인덱스 찾기
    k = graph[cur_i][cur_j].index(num)

    # 각 위치의 마지막 원소가 맨 위에 있는 원소
    graph[ni][nj] = graph[ni][nj] + graph[cur_i][cur_j][k:]
    graph[cur_i][cur_j] = graph[cur_i][cur_j][:k]
    # 테스트
    # for row in graph:
    #     print(*row)
    # print('----------')

for i in range(n):
    for j in range(n):
        if len(graph[i][j]) == 0:
            print("None")
        else:
            print(*graph[i][j][::-1])