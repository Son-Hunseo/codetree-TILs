n = int(input())

data = list(map(int, input().split()))

result = []
for i in range(n):
    result.append(data[i])
    result.sort()
    if (i+1)%2 == 1:
        print(result[(len(result)-1)//2], end=" ")