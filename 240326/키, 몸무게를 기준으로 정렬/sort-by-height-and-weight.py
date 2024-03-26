n = int(input())

data = []
for _ in range(n):
    data.append(tuple(map(str, input().split())))

data.sort(key=lambda x:(int(x[1]), -int(x[2])))

for name, h, w in data:
    print(name, h, w)