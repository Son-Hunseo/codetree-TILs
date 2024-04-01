n = int(input())
ini_i, ini_j = map(int, input().split())
# 인덱스화
cur_i, cur_j = ini_i-1, ini_j-1

graph = []
for _ in range(n):
    graph.append(list(input()))

# 오른쪽 확인의 편의를 위해 시계방향으로 정의
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def check_right(cur_i, cur_j, cur_dr):
    right_dr = (cur_dr+1)%4
    ni = cur_i + di[right_dr]
    nj = cur_j + dj[right_dr]
    if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
        return True
    elif graph[ni][nj] == "#":
        return True
    else:
        return False

def check_forward(cur_i, cur_j, cur_dr):
    ni = cur_i + di[cur_dr]
    nj = cur_j + dj[cur_dr]
    if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
        return True
    elif graph[ni][nj] == "#":
        return False
    else:
        return True

cur_dr = 1
time = 0
while True:
    if time > n*n:
        time = -1
        break
    if check_forward(cur_i, cur_j, cur_dr):
        cur_i = cur_i + di[cur_dr]
        cur_j = cur_j + dj[cur_dr]
        time += 1
        if cur_i < 0 or cur_i > n-1 or cur_j < 0 or cur_j > n-1:
            break
        elif check_right(cur_i, cur_j, cur_dr) != True:
            cur_dr = (cur_dr+1)%4

    else:
        # 방향 전환
        cur_dr = (cur_dr+3)%4

print(time)