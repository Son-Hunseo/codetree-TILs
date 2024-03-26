n = int(input())

data = list(map(int, input().split()))
data.sort()
print(*data)
data.sort(reverse=True)
print(*data)