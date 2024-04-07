n, m, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

people_graph = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    people_graph[x - 1][y - 1] += 1

# 출구
x, y = map(int, input().split())
escape = [x - 1, y - 1]
people_graph[escape[0]][escape[1]] = -99999999


def get_escape():
    for i in range(n):
        for j in range(n):
            if people_graph[i][j] < -10000:
                return [i, j]

def cal_distance(cur_x, cur_y, es_x, es_y):
    return abs(cur_x - es_x) + abs(cur_y - es_y)


# move 다시 짜야함
# 상하좌우 우선이라 방향 이런 순서로 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move():
    global move_sum
    plist = []
    for i in range(n):
        for j in range(n):
            if people_graph[i][j] >= 1:
                plist.append((i, j))

    es = get_escape()

    for i, j in plist:
        cur_dis = cal_distance(i, j, es[0], es[1])
        for dr in range(4):
            nx = i + dx[dr]
            ny = j + dy[dr]
            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1 or graph[nx][ny] >= 1:
                continue
            n_dis = cal_distance(nx, ny, es[0], es[1])
            if n_dis >= cur_dis:
                continue
            if people_graph[nx][ny] < -10000:
                move_sum += people_graph[i][j]
                people_graph[i][j] = 0
                break
            else:
                move_sum += people_graph[i][j]
                people_graph[nx][ny] = people_graph[i][j]
                people_graph[i][j] = 0
                break

def get_square():
    x, y = 0, 0
    num = 99999999
    es = get_escape()

    for i in range(n):
        for j in range(n):
            if people_graph[i][j] >= 1:
                side = max((abs(i - es[0])), abs(j - es[1]))
                if side < num:
                    num = side
                    x, y = i, j
    side = num

    # 우측 하단 구하기
    RD_x = max(x, es[0])
    RD_y = max(y, es[1])
    # 정사각형 범위 구하기
    if RD_x - side >= 0:
        LU_x = RD_x - side
    else:
        LU_x = 0
        RD_x = side
    if RD_y - side >= 0:
        LU_y = RD_y - side
    else:
        LU_y = 0
        RD_y = side
    return (LU_x, LU_y, RD_x, RD_y)


# 돌릴 때 graph 랑 people graph 같이 돌려야함
def turn_square(LU_x, LU_y, RD_x, RD_y):
    target_square = []

    # graph 돌리기
    if (RD_x - LU_x) != 0:
        for i in range(LU_x, RD_x + 1):
            target_square.append(graph[i][LU_y:RD_y + 1])
        target_square = list(map(list, zip(*target_square)))
        target_square = [row[::-1] for row in target_square]
    
        # graph에 적용
        for i in range(len(target_square)):
            for j in range(len(target_square)):
                graph[LU_x+i][LU_y+j] = max(target_square[i][j]-1, 0)
    
        target_square = []
    
        # people graph 돌리기
        for i in range(LU_x, RD_x + 1):
            target_square.append(people_graph[i][LU_y:RD_y + 1])
        target_square = list(map(list, zip(*target_square)))
        target_square = [row[::-1] for row in target_square]
    
        # people graph에 적용
        for i in range(len(target_square)):
            for j in range(len(target_square)):
                people_graph[LU_x+i][LU_y+j] = target_square[i][j]

# 시뮬레이션 시작
move_sum = 0

for _ in range(k):
    # 참가자 이동
    move()
    # 돌릴 위치 확인
    LU_x, LU_y, RD_x, RD_y = get_square()
    # 미로 회전
    turn_square(LU_x, LU_y, RD_x, RD_y)

print(move_sum)
es = get_escape()
print(es[0]+1, es[1]+1)