n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def check(i, j, k):
    global candi_list
    if ((oi - i)**2)**(1/2) + ((oj - j)**2)**(1/2) >= k:
        return
    for dr in range(4):
        ni = i + di[dr]
        nj = j + dj[dr]
        if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
            continue
        else:
            if (ni, nj) not in candi_list:
                candi_list.append((ni, nj))
                check(ni, nj, k)

def mining(candi_list, m, k):
    gold_num = 0
    for i, j in candi_list:
        if graph[i][j] == 1:
            gold_num += 1
    if gold_num*m >= (k**2 + (k+1)**2):
        return gold_num
    else:
        return 0

result = 0
for i in range(n):
    for j in range(n):
        for k in range(2*n-1):
            oi, oj = i, j
            candi_list = [(i, j)]
            check(i, j, k)
            result = max(result, mining(candi_list, m, k))

print(result)