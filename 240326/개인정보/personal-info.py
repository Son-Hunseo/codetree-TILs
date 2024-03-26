data = []

for _ in range(5):
    data.append(tuple(map(str, input().split())))

data.sort(key=lambda x:x[0])
print("name")
for name, h, w in data:
    print(name, h, w)

print("")

data.sort(key=lambda x:-int(x[1]))
print("height")
for name, h, w in data:
    print(name, h, w)