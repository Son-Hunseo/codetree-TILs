t = int(input())

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

mapping = {
    'U': 0,
    'L': 1,
    'D': 2,
    'R': 3
}


def move_marble(marble):
    marble[0] = marble[0] + dx[marble[3]]
    marble[1] = marble[1] + dy[marble[3]]
    return marble


def crash(marble1, marble2):
    if marble1[2] > marble2[2]:
        return marble1
    elif marble1[2] == marble2[2]:
        if marble1[4] > marble2[4]:
            return marble1
        else:
            return marble2
    else:
        return marble2


for _ in range(t):
    n = int(input())
    data = []
    for i in range(1, n + 1):
        x, y, w, dr = map(str, input().split())
        x, y, w, dr = (int(x) * 2) + 2000, (int(y) * 2) + 2000, int(w), mapping[dr]
        data.append([x, y, w, dr, i])

    time = 0
    result = -1
    flag = True
    while flag == True:
        time += 1
        ndata = []
        for i in range(len(data)):
            con1 = move_marble(data[i])
            if con1[0] < 0 or con1[0] > 4000 or con1[1] < 0 or con1[1] > 4000:
                flag = False
                break
            if len(ndata) == 0:
                ndata.append(con1)
            else:
                check = False
                for j in range(len(ndata)):
                    con2 = ndata[j]
                    if con1[0] == con2[0] and con1[1] == con2[1]:
                        result = time
                        ndata[j] = crash(con1, con2)
                        check = True
                if check == False:
                    ndata.append(con1)
        data = ndata[:]
    print(result)