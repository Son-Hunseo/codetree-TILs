n, m, t = map(int, input().split())

mapping = {
    "U": 0,
    "L": 1,
    "D": 2,
    "R": 3
}

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

data = []
for i in range(1, m+1):
    x, y, dr, w = map(str, input().split())
    x, y, dr, w = int(x)-1, int(y)-1, mapping[dr], int(w)
    data.append([x, y, dr, w, i])

def move_marble(marble):
    dr = marble[2]
    nx = marble[0] + dx[dr]
    ny = marble[1] + dy[dr]
    if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
        dr = (dr+2)%4
        return [marble[0], marble[1], dr, marble[3], marble[4]]
    else:
        return [nx, ny, marble[2], marble[3], marble[4]]

def crash(marble1, marble2):
    x, y, dr1, w1, num1 = marble1[0], marble1[1], marble1[2], marble1[3], marble1[4]
    x, y, dr2, w2, num2 = marble2[0], marble2[1], marble2[2], marble2[3], marble2[4]
    w = w1 + w2
    if num1 > num2:
        dr = dr1
        num = num1
    else:
        dr = dr2
        num = num2
    return [x, y, dr, w, num]

for _ in range(t):
    ndata = []
    for i in range(len(data)):
        x, y, dr, w, num = move_marble(data[i])
        if len(ndata) == 0:
            ndata.append([x, y, dr, w, num])
        else:
            check = False
            for j in range(len(ndata)):
                if x == ndata[j][0] and y == ndata[j][1]:
                    ndata[j] = crash([x, y, dr, w, num], ndata[j])
                    check = True
            if check == False:
                ndata.append([x, y, dr, w, num])
    data = ndata[:]

print(len(data), end=" ")
max_w = 0
for con in data:
    max_w = max(con[3], max_w)

print(max_w)