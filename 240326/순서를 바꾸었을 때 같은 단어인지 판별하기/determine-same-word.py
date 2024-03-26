data1 = list(input())
data2 = list(input())

data1.sort()
data2.sort()

if len(data1) != len(data2):
    print("No")
else:
    for i in range(len(data1)):
        if data1[i] != data2[i]:
            print("No")
        else:
            if i == len(data1)-1:
                print("Yes")