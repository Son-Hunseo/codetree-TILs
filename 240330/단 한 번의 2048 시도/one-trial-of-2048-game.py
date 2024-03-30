graph = []

for _ in range(4):
    graph.append(list(map(int, input().split())))

mapping = {
    "U":0,
    "L":1,
    "D":2,
    "R":3
}

dr = input()

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

# 왼쪽으로 기울이는 것 기준 (한 행)
def move(idx):
    temp = []
    for i in range(4):
        if graph[idx][i] != 0:
            temp.append(graph[idx][i])
    # 합치기
    if temp:
        for i in range(len(temp)-1):
            if temp[i] == 0:
                continue
            elif temp[i] == temp[i+1]:
                temp[i] = temp[i]*2
                temp[i+1] = 0
    
    # 사이에 남은 0 지우기
    temp2 = []
    for i in range(len(temp)):
        if temp[i] != 0:
            temp2.append(temp[i])
    
    # 남는 공간 0으로 채워주기
    cnt = len(temp2)
    while cnt < 4:
        temp2.append(0)
        cnt += 1
    
    # graph에 적용
    for i in range(4):
        graph[idx][i] = temp2[i]

if dr == "U":
    graph = list(map(list, zip(*graph)))
    for i in range(4):
        move(i)
    graph = list(map(list, zip(*graph)))
elif dr == "L":
    for i in range(4):
        move(i)
elif dr == "D":
    graph = list(map(list, zip(*graph)))
    graph = [row[::-1] for row in graph]
    for i in range(4):
        move(i)
    graph = [row[::-1] for row in graph]
    graph = list(map(list, zip(*graph)))
else:
    graph = [row[::-1] for row in graph]
    for i in range(4):
        move(i)
    graph = [row[::-1] for row in graph]

for row in graph:
    print(*row)