from collections import deque

n, m, k = map(int, input().split())

graph = [[0 for _ in range(n)] for _ in range(n)]
# 뱀의 초기 위치
graph[0][0] = 1

for _ in range(m):
    apple_x, apple_y = map(int, input().split())
    # 인덱스로
    apple_x, apple_y = apple_x-1, apple_y-1
    # 사과는 2로 표시
    graph[apple_x][apple_y] = 2

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

mapping = {
    "U": 0,
    "L": 1,
    "D": 2,
    "R": 3
}
snake = deque()
snake.append((0, 0))
time = 0
def snake_move():
    global time
    for _ in range(k):
        dr, cnt = map(str, input().split())
        cnt = int(cnt)
        dr = mapping[dr]

        for _ in range(cnt):
            ni = snake[0][0] + di[dr]
            nj = snake[0][1] + dj[dr]
            # 격자 밖
            if ni < 0 or ni > n-1 or nj < 0 or nj > n-1:
                time += 1
                return
            # 빈칸
            if graph[ni][nj] == 0:
                time += 1
                graph[ni][nj] = 1
                snake.appendleft((ni, nj))
                tail_i, tail_j = snake.pop()
                graph[tail_i][tail_j] = 0
            # 사과
            elif graph[ni][nj] == 2:
                time += 1
                graph[ni][nj] = 1
                snake.appendleft((ni, nj))
            # 꼬리 위치와 머리 위치가 바뀌는 순간
            elif ni == snake[-1][0] and nj == snake[-1][1]:
                time += 1
                snake.appendleft((ni, nj))
                tail_i, tail_j = snake.pop()
            # 몸이 꼬임
            else:
                time += 1
                return

snake_move()
print(time)