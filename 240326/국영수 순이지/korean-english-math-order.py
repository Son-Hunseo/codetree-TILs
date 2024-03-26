n = int(input())

data = []
for _ in range(n):
    data.append(tuple(map(str, input().split())))

data.sort(key=lambda x:(x[1], x[2], x[3]), reverse=True)

for name, guk, eng, math in data:
    print(name, guk, eng, math)