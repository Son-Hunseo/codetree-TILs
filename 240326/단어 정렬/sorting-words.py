n = int(input())
data = []
for _ in range(n):
    data.append(input())

data.sort()
for con in data:
    print(con)