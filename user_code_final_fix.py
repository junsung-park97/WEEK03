# 1이든 2이든 3이든 정점의 노드명이 들어오면 그 노드명의 - 1 인덱스의 간선 1 추가해서 위상정렬로 풀면 끝
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

#인접리스트와 인접차수를 넣을 곳 만들기
graph = [[] for _ in range(n + 1)]
in_gree = [0] * (n + 1)

#그래프 요소를 입력받아 넣기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_gree[b] += 1

print(f'graph: {graph}, in_gree:{in_gree}')

# 큐를 초기화하고 진입차수가 0인 노드들을 큐에 추가함
queue = deque([])

# 수정 1: 정점 번호로 순회하고, 진입차수가 0인 정점을 큐에 추가
for node in range(1, n + 1):  # 정점 번호 1, 2, 3, ... 순회
    if in_gree[node] == 0:    # 해당 정점의 진입차수가 0인지 확인
        queue.append(node)    # 정점 번호를 큐에 추가

print(f'초기 큐: {list(queue)}')

result = []

while queue:
    current = queue.popleft()
    result.append(current)
    print(f'현재 처리 중인 정점: {current}')

    for neighbor in graph[current]:
        print(f'  인접 정점 {neighbor}의 진입차수: {in_gree[neighbor]} → {in_gree[neighbor] - 1}')
        in_gree[neighbor] -= 1
        
        # 수정 2: 정점 번호(neighbor)를 큐에 추가
        if in_gree[neighbor] == 0:
            queue.append(neighbor)  # neighbor를 큐에 추가 (in_gree[neighbor] 아님!)
            print(f'  정점 {neighbor}를 큐에 추가')

print(f'최종 결과: {result}')

# 백준 제출용 (디버깅 출력 제거)
# print(' '.join(map(str, result))) 