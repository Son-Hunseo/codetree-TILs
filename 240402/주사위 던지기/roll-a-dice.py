n, m, r, c = map(int, input().split())
# 인덱스화
r, c = r-1, c-1

dr_data = list(map(str, input().split()))

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

mapping = {
    "U": 0,
    "L": 1,
    "D": 2,
    "R": 3
}

def get_next_dice(F, U, R, dr):
    if dr == 0:
        nF = 7-U
        nU = F
        nR = R
    elif dr == 1:
        nF = F
        nU = R
        nR = 7-U
    elif dr == 2:
        nF = U
        nU = 7-F
        nR = R
    else:
        nF = F
        nU = 7-R
        nR = U
    return nF, nU, nR

F = 2
U = 1
R = 3

# ULDR 을 0123으로 바꿈
for i in range(len(dr_data)):
    dr_data[i] = mapping[dr_data[i]]

graph = [[0 for _ in range(n)] for _ in range(n)]
graph[r][c] = 7-U

for dr in dr_data:
    ni = r + di[dr]
    nj = c + dj[dr]
    if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
        continue
    F, U, R = get_next_dice(F, U, R, dr)
    graph[ni][nj] = 7-U
    r, c = ni, nj

result = 0
for row in graph:
    result += sum(row)

print(result)