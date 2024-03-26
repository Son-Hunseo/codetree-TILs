n = int(input())

datas = []
for i in range(n):
    data = tuple(map(int, input().split()))
    data = (data[0], data[1], i+1)
    datas.append(data)

datas.sort(key=lambda x:x[0]**2 + x[1]**2)

for _, _, num in datas:
    print(num)