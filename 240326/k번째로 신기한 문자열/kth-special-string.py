n, k, t = map(str, input().split())
n, k = int(n), int(k)

data = []
for _ in range(n):
    check = True
    word = input()
    if len(t) > len(word):
        check = False
    else:
        for j in range(len(t)):
            if t[j] != word[j]:
                check = False
    if check == True:
        data.append(word)

data.sort()
print(data[k-1])