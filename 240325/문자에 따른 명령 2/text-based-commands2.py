data = input()

di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

cur_i, cur_j = 0, 0
cur_dr = 0

for i in range(len(data)):
    if data[i] == "L":
        if cur_dr == 0:
            cur_dr = 2
        elif cur_dr == 1:
            cur_dr = 3
        elif cur_dr == 2:
            cur_dr = 1
        elif cur_dr == 3:
            cur_dr = 0
    if data[i] == "R":
        if cur_dr == 0:
            cur_dr = 3
        elif cur_dr == 1:
            cur_dr = 2
        elif cur_dr == 2:
            cur_dr = 0
        elif cur_dr == 3:
            cur_dr = 1
    if data[i] == "F":
        cur_i += di[cur_dr]
        cur_j += dj[cur_dr]

print(cur_j, end=" ")
print(cur_i)