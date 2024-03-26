n = int(input())

datas = []
for i in range(n):
    data = tuple(map(int, input().split()))
    datas.append((data[0], data[1], i+1))

datas.sort(key=lambda x:(x[0], -x[1]))

for h, w, num in datas:
    print(h, w, num)