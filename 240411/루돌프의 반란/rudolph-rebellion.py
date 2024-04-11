from collections import deque

# 입력
n, m, p, c, d = map(int, input().split())

Rr, Rc = map(int, input().split())
Rr, Rc = Rr-1, Rc-1

# (r, c, 기절여부)
santa_data = [(-1, -1, 9999) for _ in range(p+1)]
for i in range(1, p+1):
    Snum, Sr, Sc = map(int, input().split())
    santa_data[Snum] = (Sr-1, Sc-1, 0)

# 루돌프 방향, 산타 방향, 현재 루돌프 방향, 산타 현재 방향 정의
Rdx = [-1, -1, 0, 1, 1, 1, 0, -1]
Rdy = [0, 1, 1, 1, 0, -1, -1, -1]

Sdx = [-1, 0, 1, 0]
Sdy = [0, 1, 0, -1]

Rdr = -1
Sdr = -1

# 산타 점수표
score = [0 for _ in range(p+1)]

# 거리 계산
def cal_distance(r1, c1, r2, c2):
    return (r1 - r2) ** 2 + (c1 - c2) ** 2

# 루돌프 이동
def Ru_move():
    global Rr, Rc, Rdr

    # 돌진대상이 될 산타 찾기
    ## (번호, 거리, r, c)
    santa_dis = [(0, 9999, -1, -1) for _ in range(p+1)]
    for i in range(1, len(santa_data)):
        santa_dis[i] = (i, cal_distance(Rr, Rc, santa_data[i][0], santa_data[i][1]), santa_data[i][0], santa_data[i][1])
    santa_dis.sort(key=lambda x: (x[1], -x[2], -x[3]))
    target_santa = santa_dis[0]
    Tr, Tc = target_santa[2], target_santa[3]

    # 돌진할 방향 정하기
    dr_dis = [9999 for _ in range(8)]
    for dr in range(8):
        nRr = Rr + Rdx[dr]
        nRc = Rc + Rdy[dr]
        dr_dis[dr] = cal_distance(Tr, Tc, nRr, nRc)
    dr = dr_dis.index(min(dr_dis)) # 루돌프가 돌진할 방향

    # 이동
    Rr = Rr + Rdx[dr]
    Rc = Rc + Rdy[dr]
    Rdr = dr

def santa_move(num):
    global Sdr
    sx, sy, is_stun = -1, -1, -1
    if santa_data[num]:
        sx, sy, is_stun = santa_data[num][0], santa_data[num][1], santa_data[num][2]

    # 기절한 경우
    if is_stun != 0:
        if is_stun == -1:
            return (sx, sy, -1)
        return (sx, sy, is_stun - 1)
    # 탈락한 경우
    elif sx == -1 and sy == -1 and is_stun == -1:
        return False
    # 기절하지 않고 존재하는 경우
    else:
        cur_dis = cal_distance(Rr, Rc, sx, sy)
        dr_dis = [9999 for _ in range(4)]
        for dr in range(4):
            is_santa = False
            nsx = sx + Sdx[dr]
            nsy = sy + Sdy[dr]
            # 격자 밖으로 이동할 수 없다.
            if nsx < 0 or nsx > n-1 or nsy < 0 or nsy > n-1:
                continue
            # 이미 산타가 존재하는 곳으로 이동할 수 없다.
            for santa in santa_data:
                if nsx == santa[0] and nsy == santa[1]:
                    is_santa = True
                    break
            if is_santa == True:
                continue
            # 현재 방향으로 이동했을 때의 루돌프와의 거리 계산
            ndis = cal_distance(Rr, Rc, nsx, nsy)
            if ndis < cur_dis:
                dr_dis[dr] = ndis
        # 더 가까워지는 방향이 없는 경우 -> 움직일 수 없는 경우
        if min(dr_dis) == 9999:
            return (sx, sy, is_stun)
        # 더 가까워지는 방향이 있는 경우
        else:
            dr = dr_dis.index(min(dr_dis))
            sx = sx + Sdx[dr]
            sy = sy + Sdy[dr]
            Sdr = dr
            return (sx, sy, is_stun)

def crash(tern):
    global cur_crash_santa_num
    for i in range(1, len(santa_data)):
        if santa_data[i][0] == Rr and santa_data[i][1] == Rc:
            cur_crash_santa_num = i
            # 루돌프 턴: 0 -> 즉, 루돌프가 충돌
            if tern == 0:
                score[i] += c
                nsx = santa_data[i][0] + (Rdx[Rdr] * c)
                nsy = santa_data[i][1] + (Rdy[Rdr] * c)
                if nsx < 0 or nsx > n-1 or nsy < 0 or nsy > n-1:
                    santa_data[i] = (-1, -1, -1)
                else:
                    # 루돌프의 경우 산타 턴을 한번 순회해야하기 때문에 2로 해줬다.
                    santa_data[i] = (nsx, nsy, 2)
            # 산타 턴 -> 즉, 산타 충돌
            else:
                score[i] += d
                nsx = santa_data[i][0] + (Sdx[(Sdr + 2) % 4] * d)
                nsy = santa_data[i][1] + (Sdy[(Sdr + 2) % 4] * d)
                if nsx < 0 or nsx > n - 1 or nsy < 0 or nsy > n - 1:
                    santa_data[i] = (-1, -1, -1)
                else:
                    santa_data[i] = (nsx, nsy, 1)

def interaction(turn):
    global S_dr
    global R_dr
    global cur_crash_santa_num

    # 아무도 부딫히지 않은 경우 (아무도 이동이 없으니 산타가 튕겨져 상호작용이 일어날 일도 없다)
    if cur_crash_santa_num == -9999:
        return

    q = deque()
    # 탈락한 산타라면
    if santa_data[cur_crash_santa_num][0] == -1 and santa_data[cur_crash_santa_num][1] == -1 and santa_data[cur_crash_santa_num][2] == -1:
        return
    # 탈락한 산타가 아니라면
    q.append(santa_data[cur_crash_santa_num])

    # 연쇄작용
    while q:
        cur_x, cur_y, is_stun = q.popleft()
        santa_data[cur_crash_santa_num] = (cur_x, cur_y, is_stun)
        origin_crash_santa_num = cur_crash_santa_num
        for i in range(len(santa_data)):
            # 현재 산타 자신은 스킵
            if i == origin_crash_santa_num:
                continue
            if santa_data[i][0] == cur_x and santa_data[i][1] == cur_y:
                cur_crash_santa_num = i
                # 루돌프 턴: 0
                if turn == 0:
                    nx = cur_x + Rdx[Rdr]
                    ny = cur_y + Rdy[Rdr]
                # 산타 턴
                else:
                    nx = cur_x + Sdx[(Sdr+2)%4]
                    ny = cur_y + Sdy[(Sdr+2)%4]

                if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                    santa_data[cur_crash_santa_num] = (-1, -1, -1)
                    continue
                q.append((nx, ny, santa_data[i][2]))


for cnt in range(m):
    Ru_move()
    cur_crash_santa_num = -9999
    crash(0)
    interaction(0)
    for i in range(1, p+1):
        santa_data[i] = santa_move(i)
        cur_crash_santa_num = -9999
        crash(1)
        interaction(1)
    for i in range(len(score)):
        # 탈락인 경우
        if santa_data[i][0] == -1 and santa_data[i][1] == -1:
            continue
        # 생존한 경우
        score[i] += 1

print(*score[1:])