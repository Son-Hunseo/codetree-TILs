n = int(input())
data = list(map(int, input().split()))

data.sort()
result = []

for i in range(n):
    result.append(data[i]+data[-(i+1)])

print(max(result))