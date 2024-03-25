cur_i, cur_j = 0, 0
dr = 0

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

data = input()

time = 0
first = True
for i in range(len(data)):
    if first == False and cur_i == 0 and cur_j == 0:
        break
    if data[i] == "L":
        time += 1
        dr = (dr+1)%4
    elif data[i] == "R":
        time += 1
        dr = (dr+3)%4
    else:
        time += 1
        cur_i = cur_i + di[dr]
        cur_j = cur_j + dj[dr]
    first = False

if cur_i == 0 and cur_j == 0:
    print(time)
else:
    print(-1)