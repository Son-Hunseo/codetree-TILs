n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append(int(input()))

def bomb():
    global data
    cur = 999
    candi = []
    for i in range(len(data)-1, -1, -1):
        if data[i] != cur:
            if len(candi) >= m:
                for idx in candi:
                    data[idx] = 0
            candi = []
            candi.append(i)
            cur = data[i]
        else:
            candi.append(i)
        if i == 0:
            if len(candi) >= m:
                for idx in candi:
                    data[idx] = 0

def fall_down():
    global data
    temp = []
    for i in range(len(data)):
        if data[i] != 0:
            temp.append(data[i])
    data = temp

for _ in range(n):
    bomb()
    fall_down()

if data:
    print(len(data))
    for con in data:
        print(con)
else:
    print(0)