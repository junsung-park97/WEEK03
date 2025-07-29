# 백준 2252번 줄 세우기 - 위상정렬
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

# 인접리스트와 진입차수를 넣을 곳 만들기
graph = [[] for _ in range(n + 1)]
in_gree = [0] * (n + 1)

# 그래프 요소를 입력받아 넣기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_gree[b] += 1

# 큐를 초기화하고 진입차수가 0인 노드들을 큐에 추가함
queue = deque([])
for node in range(1, n + 1):
    if in_gree[node] == 0:
        queue.append(node)

result = []

while queue:
    current = queue.popleft()
    result.append(current)

    for neighbor in graph[current]:
        in_gree[neighbor] -= 1
        if in_gree[neighbor] == 0:
            queue.append(neighbor)

# 백준 제출용 출력 형식
print(' '.join(map(str, result))) 