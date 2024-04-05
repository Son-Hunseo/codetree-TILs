t = int(input())

mapping = {
    "U": 0,
    "L": 1,
    "D": 2,
    "R": 3
}

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(t):
    n = int(input())
    data = []
    for i in range(1, n+1):
        x, y, w, dr = map(str, input().split())
        x, y, w = 2000+(int(x)*2), 2000+(int(y)*2), int(w)
        dr = mapping[dr]
        data.append([x, y, w, dr, i])
    
    time = 0
    result = -1

    while data:
        ndata = []
        time += 1
        for con1 in data:
            x, y, w, dr, num = con1[0], con1[1], con1[2], con1[3], con1[4]
            nx, ny = x + dx[dr], y + dy[dr]
            if x > 4000 or y > 4000 or x < 0 or y < 0:
                data.remove(con1)
                break
            if ndata:
                check = False
                for con2 in ndata:
                    if nx == con2[0] and ny == con2[1]:
                        check = True
                        result = time
                        if w > con2[2]:
                            ndata.remove(con2)
                            ndata.append([nx, ny, w, dr, num])
                        elif w == con2[2]:
                            if num > con2[4]:
                                ndata.remove(con2)
                                ndata.append([nx, ny, w, dr, num])
                if check == False:
                    ndata.append([nx, ny, w, dr, num])
            else:
                ndata.append([nx, ny, w, dr, num])
        data = ndata[:]
    print(result)