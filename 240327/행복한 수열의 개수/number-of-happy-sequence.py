n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def check(idx, method):
    if method == "row":
        cnt = 1
        bf_num = 0
        for i in range(n):
            if graph[idx][i] == bf_num:
                cnt += 1
                if cnt == m:
                    return 1
            else:
                bf_num = graph[idx][i]
                cnt = 1
                if cnt == m:
                    return 1
    else:
        cnt = 1
        bf_num = 0
        for i in range(n):
            if graph[i][idx] == bf_num:
                cnt += 1
                if cnt == m:
                    return 1
            else:
                bf_num = graph[i][idx]
                cnt = 1
                if cnt == m:
                    return 1
    return 0

result = 0
for i in range(n):
    result += check(i, "row")
    result += check(i, "col")

print(result)