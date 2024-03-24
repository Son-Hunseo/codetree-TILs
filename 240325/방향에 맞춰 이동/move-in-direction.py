n = int(input())

di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

cur_i, cur_j = 0, 0

for _ in range(n):
    dr, cnt = map(str, input().split())
    cnt = int(cnt)
    if dr == "N":
        cur_i += di[0]*cnt
        cur_j += dj[0]*cnt
    if dr == "S":
        cur_i += di[1]*cnt
        cur_j += dj[1]*cnt
    if dr == "W":
        cur_i += di[2]*cnt
        cur_j += dj[2]*cnt
    if dr == "E":
        cur_i += di[3]*cnt
        cur_j += dj[3]*cnt

result = []
result.append(cur_j)
result.append(cur_i)
print(*result)