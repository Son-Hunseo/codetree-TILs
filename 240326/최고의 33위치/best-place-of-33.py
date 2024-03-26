n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def check(cur_i, cur_j):
    cnt = 0
    for i in range(cur_i, cur_i+3):
        for j in range(cur_j, cur_j+3):
            if graph[i][j] == 1:
                cnt += 1
    return cnt

max_num = 0
for i in range(0, n-2):
    for j in range(0, n-2):
        max_num = max(max_num, check(i, j))

print(max_num)