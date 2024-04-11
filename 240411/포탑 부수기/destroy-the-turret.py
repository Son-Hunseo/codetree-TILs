from collections import deque

n, m, k = map(int, input().split())

graph = []
for _ in range(n):
    data = list(map(int, input().split()))
    for i in range(m):
        # 마지막으로 공격한 턴 기록
        data[i] = (data[i], 0)
    graph.append(data)

def select_attacker():
    min_value = 9999
    # 일단 최솟값 정하기
    for i in range(n):
        for j in range(m):
            if graph[i][j][0] == 0:
                continue
            min_value = min(min_value, graph[i][j][0])
    # 그 값을 가지는 후보군들 정하기
    candi = []
    for i in range(n):
        for j in range(m):
            if graph[i][j][0] == min_value:
                # (마지막으로 공격했던 턴, 행, 열)
                candi.append((graph[i][j][1], i, j))
    # 기준에 맞게 정렬
    candi.sort(key=lambda x:(-x[0], -(x[1]+x[2]), -x[2]))
    attacker = candi[0]
    return (attacker[1], attacker[2])

def select_target(attacker_i, attacker_j):
    max_value = -9999
    # 일단 최댓값 정하기 (현재 공격자 제외)
    for i in range(n):
        for j in range(m):
            if i == attacker_i and j == attacker_j:
                continue
            if graph[i][j][0] == 0:
                continue
            max_value = max(max_value, graph[i][j][0])
    # 그 값을 가지는 후보군들 정하기
    candi = []
    for i in range(n):
        for j in range(m):
            if graph[i][j][0] == max_value:
                # (마지막으로 공격했던 턴, 행, 열)
                candi.append((graph[i][j][1], i, j))
    # 기준에 맞게 정렬
    candi.sort(key=lambda x: (x[0], x[1] + x[2], x[2]))
    target = candi[0]
    return (target[1], target[2])

# 우하좌상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def laser(attacker_i, attacker_j, target_i, target_j):
    # 새로운 격자를 생성하여 파괴된 포탑을 벽처럼 9999로 표시
    ngraph = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j][0] == 0:
                ngraph[i][j] = 9999
    # bfs
    q = deque()
    q.append((attacker_i, attacker_j))
    ngraph[attacker_i][attacker_j] = 1

    while q:
        cur_i, cur_j = q.popleft()
        for dr in range(4):
            ni = cur_i + di[dr]
            nj = cur_j + dj[dr]
            # 반대편으로 넘어가는 것 처리
            if ni < 0:
                ni = n + ni
            elif ni > n-1:
                ni = ni - n
            if nj < 0:
                nj = m + nj
            elif nj > m-1:
                nj = nj - m
            # 방문 했거나 부서진 포탑의 경우 못감
            if ngraph[ni][nj] != 0 or ngraph[ni][nj] == 9999:
                continue
            # 위의 경우가 아니라면 방문 처리 후 queue에 넣기
            ngraph[ni][nj] = ngraph[cur_i][cur_j] + 1
            q.append((ni, nj))

    target_value = ngraph[target_i][target_j]
    # 갈 수 없는 경로라면 False 리턴
    if target_value == 0:
        return False

    # 조건에 맞는 경로 찾기
    road = [(target_i, target_j)]
    cur_i, cur_j = target_i, target_j
    is_start = False
    while True:
        if is_start == True:
            break
        for dr in range(3, -1, -1):
            bi = cur_i + di[dr]
            bj = cur_j + dj[dr]
            if bi < 0:
                bi = n + bi
            elif bi > n-1:
                bi = bi - n
            if bj < 0:
                bj = m + bj
            elif bj > m-1:
                bj = bj - m
            if ngraph[bi][bj] == ngraph[cur_i][cur_j] - 1:
                road.append((bi, bj))
                cur_i, cur_j = bi, bj
                if cur_i == attacker_i and cur_j == attacker_j:
                    is_start = True
                break
    # 공격자 포탑 제외
    road.pop()
    return road


bdi = [-1, -1, 0, 1, 1, 1, 0, -1]
bdj = [0, 1, 1, 1, 0, -1, -1, -1]
def bomb(attacker_i, attacker_j, target_i, target_j):
    # 새로운 격자를 생성하여 파괴된 포탑을 벽처럼 9999로 표시
    ngraph = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j][0] == 0:
                ngraph[i][j] = 9999

    road = [(target_i, target_j)]
    for dr in range(8):
        ni = target_i + bdi[dr]
        nj = target_j + bdj[dr]
        if ni < 0:
            ni = n + ni
        elif ni > n - 1:
            ni = ni - n
        if nj < 0:
            nj = m + nj
        elif nj > m - 1:
            nj = nj - m
        # 부서진 포탑이거나 공격자 포탑이면 영향 못미침
        if ngraph[ni][nj] == 9999:
            continue
        if ni == attacker_i and nj == attacker_j:
            continue
        road.append((ni, nj))
    return road


def attack(attacker_i, attacker_j, target_i, target_j):
    if laser(attacker_i, attacker_j, target_i, target_j) != False:
        road = laser(attacker_i, attacker_j, target_i, target_j)
    else:
        road = bomb(attacker_i, attacker_j, target_i, target_j)
    return road

# k 턴동안 반복
for turn in range(1, k+1):
    attacker_i, attacker_j = select_attacker()
    target_i, target_j = select_target(attacker_i, attacker_j)
    attacker_dmg = graph[attacker_i][attacker_j][0] + n + m
    graph[attacker_i][attacker_j] = (attacker_dmg, turn)
    # 공격
    road = attack(attacker_i, attacker_j, target_i, target_j)
    for i in range(len(road)):
        if i == 0:
            graph[road[i][0]][road[i][1]] = (max(graph[road[i][0]][road[i][1]][0] - attacker_dmg, 0), graph[road[i][0]][road[i][1]][1])
        else:
            graph[road[i][0]][road[i][1]] = (max(graph[road[i][0]][road[i][1]][0] - (attacker_dmg//2), 0), graph[road[i][0]][road[i][1]][1])
    # 공격하지도 않고 받지도 않은 포탑들 공격력 1 증가
    for i in range(n):
        for j in range(m):
            if (i, j) not in road:
                if (i, j) != (attacker_i, attacker_j):
                    if graph[i][j][0] != 0:
                        graph[i][j] = (graph[i][j][0] + 1, graph[i][j][1])

    # 남은 포탑이 1개일 경우 즉시 종료
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j][0] != 0:
                cnt += 1
    if cnt == 1:
        break

    # 디버그
    # for row in graph:
    #     print(*row)
    # print("----------")

# 가장 공격력이 높은 포탑의 공격력 출력
max_dmg = 0
for i in range(n):
    for j in range(m):
        max_dmg = max(max_dmg, graph[i][j][0])

print(max_dmg)