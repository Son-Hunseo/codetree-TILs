n = int(input())
data1 = list(map(int, input().split()))
data2 = list(map(int, input().split()))

data1.sort()
data2.sort()

for i in range(n):
    if data1[i] != data2[i]:
        print("No")
        break
    if i == n-1:
        if data1[i] == data2[i]:
            print("Yes")