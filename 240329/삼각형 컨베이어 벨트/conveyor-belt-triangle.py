n, t = map(int, input().split())

data = list(map(int, input().split()))
for _ in range(2):
    data = data + list(map(int, input().split()))

def moving():
    temp = data[3*n-1]
    for i in range(3*n-1, 0, -1):
        data[i] = data[i-1]
    data[0] = temp

for _ in range(t):
    moving()

for i in range(3*n):
    if (i+1)%3 == 0:
        print(data[i])
    else:
        print(data[i], end=" ")