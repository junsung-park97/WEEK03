import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

distance = [[0] * m for _ in range(n)]

queue = deque()

queue.append((0, 0))
distance[0][0] = 1

while queue:
    x, y = queue.popleft()
    print(f'x: {x}, y: {y}')

    if x == n - 1 and y == n - 1:
        print(distance[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] == 1 and distance[nx][ny] == 0:

            distance[nx][ny] = distance[x][y] + 1
            queue.append((nx, ny))
            print(f'nx : {nx}, ny : {ny}')

