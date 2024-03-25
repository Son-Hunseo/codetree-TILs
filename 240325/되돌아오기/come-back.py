n = int(input())

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

mapping = {
    "N": 0,
    "W": 1,
    "S": 2,
    "E": 3
}
first = True
cur_i, cur_j = 0, 0
result = 0

for _ in range(n):
    if first == False and cur_i == 0 and cur_j == 0:
        break
        
    dr, cnt = map(str, input().split())
    cnt = int(cnt)

    for _ in range(cnt):
        if first == False and cur_i == 0 and cur_j == 0:
            print(result)
            break
        else:
            cur_i = cur_i + di[mapping[dr]]
            cur_j = cur_j + dj[mapping[dr]]
            result += 1
            first = False

if result == n:
    print(-1)