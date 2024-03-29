data = list(input())

def encoding(data):
    ndata = []
    cur = data[0]
    cnt = 1
    for i in range(1, len(data)):
        if data[i] == cur:
            cnt += 1
        else:
            ndata.append(cur)
            ndata.append(cnt)
            cnt = 1
            cur = data[i]
        if i == len(data)-1:
            ndata.append(cur)
            ndata.append(cnt)
    return ndata

result = []
for _ in range(len(data)):
    data = [data[-1]] + data[:len(data)-1]
    result.append(len(encoding(data)))

if result:
    print(min(result))
else:
    print(2)