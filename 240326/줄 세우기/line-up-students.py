n = int(input())

datas = []
for i in range(n):
    data = tuple(map(int, input().split()))
    data = (data[0], data[1], i+1)
    datas.append(data)

datas.sort(key=lambda x:(-x[0], -x[1], x[2]))

for h, w, num in datas:
    print(h, w, num)