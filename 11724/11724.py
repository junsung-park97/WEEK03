import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

#정점과 간선의 개수
n, m =map(int, input().split())
#그래프 선언
graph = [[] for _ in range(n + 1)]

# 각 정점과 간선의 입력 -> 그래프로 변환
for _ in range(m):  
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

#방문배열 선언
visited = [False] * (n + 1)

# dfs로직
# 지금 현재 방문한 노드를 방문배열에서 true로 바꾸고,
# 현재 노드의 인접노드를 반복하면서 그 인접노드의 방문배열값이 false이면
# dfs함수를 인접노드를 현재노드로 재귀시킨다.
def dfs(node):
    visited[node] = True

    for neighbor in graph[node]:
        # not => Falsy
        if not visited[neighbor]:
            dfs(neighbor)

# 연결정점의 카운트
count = 0

# 정점의 개수만큼 반복하면서 
# 정점마다 방문배열이 false이면 dfs함수를 실행하고, 
# 연결정점의 카운트를 1 더한다.
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i) # 새로운 연결요소 확인
        count += 1

print(count)