n = int(input())

datas = []
data = list(map(int, input().split()))
for i in range(len(data)):
    datas.append((data[i], i))

datas.sort(key=lambda x:(x[0], [1]))

result = [0] * n
for i, con in enumerate(datas):
    result[con[1]] = i + 1

print(*result)