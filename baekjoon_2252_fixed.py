import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    
    # 1. 그래프와 진입차수 배열 초기화
    graph = [[] for _ in range(n + 1)]  # 인접 리스트
    in_degree = [0] * (n + 1)           # 진입차수 배열
    
    # 2. 간선 정보 입력 및 그래프 구성
    for _ in range(m):
        a, b = map(int, input().split())  # a가 b보다 앞에 서야 함
        graph[a].append(b)                # a → b 간선 추가
        in_degree[b] += 1                 # b의 진입차수 증가
    
    # 3. 진입차수가 0인 정점들을 큐에 추가
    queue = deque()
    for node in range(1, n + 1):
        if in_degree[node] == 0:          # 진입차수가 0인 정점
            queue.append(node)
    
    # 4. 위상정렬 수행
    result = []
    
    while queue:
        current = queue.popleft()         # 현재 처리할 정점
        result.append(current)            # 결과에 추가
        
        # 현재 정점에서 나가는 간선들 처리
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1      # 인접 정점의 진입차수 감소
            if in_degree[neighbor] == 0:  # 진입차수가 0이 되면
                queue.append(neighbor)    # 큐에 추가
    
    # 5. 결과 출력
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    solve() 