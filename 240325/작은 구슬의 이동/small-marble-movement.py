n, t = map(int, input().split())

i, j, dr = map(str, input().split())
i = int(i)-1
j = int(j)-1

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

mapping = {
    "U":0,
    "D":1,
    "L":2,
    "R":3
}

cnt = 0
while cnt != t:
    cnt += 1

    ni = i+di[mapping[dr]]
    nj = j+dj[mapping[dr]]

    if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
        if dr == "U":
            dr = "D"
        elif dr == "D":
            dr = "U"
        elif dr == "L":
            dr = "R"
        else:
            dr = "L"
        continue
    else:
        i = ni
        j = nj

print(i+1, end=" ")
print(j+1)