n = int(input())
data = []

for _ in range(n):
    data.append(tuple(map(str, input().split())))

data.sort(key=lambda x: int(x[1])+int(x[2])+int(x[3]))

for name, one, two, three in data:
    print(name, one, two, three)