n = int(input())

data = []
for _ in range(n):
    data.append(tuple(map(str, input().split())))

data.sort(key=lambda x: x[1])

for name, height, weight in data:
    print(name, height, weight)