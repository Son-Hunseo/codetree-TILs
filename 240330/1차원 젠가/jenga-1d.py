n = int(input())

block = []
for _ in range(n):
    block.append(int(input()))

def block_del(s, e):
    global block
    for i in range(s, e+1):
        block[i] = 0
    temp = []
    temp_end_idx = 0
    for i in range(len(block)):
        if block[i] != 0:
            temp.append(block[i])
            temp_end_idx += 1
    block = temp

s1, e1 = map(int, input().split())
# 순서를 인덱스로 바꿈
s1, e1 = s1-1, e1-1
block_del(s1, e1)

s2, e2 = map(int, input().split())
# 순서를 인덱스로 바꿈
s2, e2 = s2-1, e2-1
block_del(s2, e2)

print(len(block))
if block:
    for con in block:
        print(con)