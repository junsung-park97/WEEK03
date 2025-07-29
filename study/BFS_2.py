# BFS(그래프, 시작정점)
# 1. 방문배열 = [False] * 정점개수
# 2. 큐 = 빈큐()
# 3. 결과 = 빈리스트()

# 4. 큐에 시작정점 추가
# 5. 방문배열[시작정점] = True

# 6. while 큐가 비어있지 않음:
# 7.     현재정점 = 큐에서 제거()
# 8.     결과에 현재정점 추가
# 9.     
# 10.    for 인접정점 in 그래프[현재정점]:
# 11.        if 방문배열[인접정점] == False:
# 12.            방문배열[인접정점] = True
# 13.            큐에 인접정점 추가
from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

def bfs (graph, start, n):

    visited = [False] * n
    queue = deque([])
    result = []

    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            if visited[neighbor] == False:
                visited[neighbor] == True
                queue.append(neighbor)