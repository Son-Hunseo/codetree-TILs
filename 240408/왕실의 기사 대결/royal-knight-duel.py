l, n, q = map(int, input().split())

graph = []
for _ in range(l):
    graph.append(list(map(int, input().split())))

knight_hp = [0 for _ in range(n+1)]
knight_loca_data = [[] for _ in range(n+1)]
for i in range(1, n+1):
    r, c, h, w, k = map(int, input().split())
    r, c = r-1, c-1
    for x in range(r, r+h):
        for y in range(c, c+w):
            knight_loca_data[i].append((x, y))
    knight_hp[i] = k

# 초기 기사 체력 데이터 저장
og_knight_hp = knight_hp[:]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def is_move(num, dr):
    for con in knight_loca_data[num]:
        x = con[0]
        y = con[1]
        nx = x + dx[dr]
        ny = y + dy[dr]
        if nx < 0 or nx > l-1 or ny < 0 or ny > l-1 or graph[nx][ny] == 2:
            return False
        for i in range(len(knight_loca_data)):
            if i == num:
                continue
            if (nx, ny) in knight_loca_data[i]:
                if is_move(i, dr) == False:
                    return False
    return True

def move(num, dr):
    for con in knight_loca_data[num]:
        x = con[0]
        y = con[1]
        nx = x + dx[dr]
        ny = y + dy[dr]
        nknight_loca_data[num].append((nx, ny))
        for i in range(len(knight_loca_data)):
            if i == num:
                continue
            if (nx, ny) in knight_loca_data[i]:
                move(i, dr)

    # 움직인 기사만 체크
    for i in range(1, n+1):
        if nknight_loca_data[i]:
            move_knight_list[i] = 1

# 명령 실행
for _ in range(q):
    num, dr = map(int, input().split())

    # 사라진 기사 반응 x
    if len(knight_loca_data[num]) == 0:
        continue

    # 움직일 수 있는지
    if is_move(num, dr) == False:
        continue
    else:
        nknight_loca_data = [[] for _ in range(n+1)]
        move_knight_list = [0 for _ in range(n+1)]
        move(num, dr)

        # 움직이지 않은 것도 처리
        for i in range(len(move_knight_list)):
            if move_knight_list[i] == 0:
                nknight_loca_data[i] = knight_loca_data[i][:]

        # 반영
        knight_loca_data = [row[:] for row in nknight_loca_data]

        # 데미지
        for i in range(1, n+1):
            # 움직인 기사이며, 현재 명령을 받은 기사가 아닐 경우에만 데미지 받음
            if move_knight_list[i] == 1 and i != num:
                for con in knight_loca_data[i]:
                    x, y = con[0], con[1]
                    if graph[x][y] == 1:
                        knight_hp[i] -= 1
        # hp가 0 이하인 기사 제거
        for i in range(1, n+1):
            if knight_hp[i] <= 0:
                knight_loca_data[i] = []

    # 테스트
    # for row in knight_loca_data:
    #     print(row)
    # print(move_knight_list)
    # print(knight_hp)
    # print("-----------")

result = 0
for i in range(1, n+1):
    # 현재 생존한 기사만 카운트
    if knight_hp[i] != 0:
        result += og_knight_hp[i] - knight_hp[i]

print(result)