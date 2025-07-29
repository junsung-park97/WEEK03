from collections import deque

def dfs(graph, start, visited):
    
    # print(f'graph:{graph}, start:{start}, visited:{visited}')
    #방문한 정점이 ture라면
    visited[start] = True
    print(start, end=' ')
    
    # # 인접한 노드를 오름차순으로 방문
    # start가 갈수있는 정점중에 반복하겠다.
    for neighbor in sorted(graph[start]):
        #그 정점중에 방문되지않은 정점이 있다면
        if not visited[neighbor]:
            #재귀를 한번 더 돌리겠다
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    # 그래프의 길이만큼 방문자체크용 리스트
    visited = [False] * (len(graph))
    # 지금 내가있는 위치의 정점을 큐에넣는다?
    queue = deque([start])
    #그리고 그 큐는 지금 ture이다?
    visited[start] = True
    
    #큐에 요소가 있는동안 반복인데
    while queue:
        #여기서 큐를 바로 빼버려.. 만약 큐에 하나만 있으면 어쩌려고..
        node = queue.popleft()
        print(node, end=' ')
        
        # 인접한 노드를 오름차순으로 큐에 추가
        #현재 정점에서 방문가능한 정점을 확인하고 반복하겠다.
        for neighbor in sorted(graph[node]):
            #방문한 정점이 false이면
            if not visited[neighbor]:
                # 그 정점을 ture로 바꾸겠다
                visited[neighbor] = True
                # 그리고 그 정점을 큐에 추가한다.
                queue.append(neighbor)

# 입력 받기
n, m, v = map(int, input().rstrip().split())

# 그래프 초기화 (인덱스 1부터 사용)
graph = [[] for _ in range(n + 1)]

# 간선 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 실행
visited = [False] * (n + 1)
dfs(graph, v, visited)
print()

# BFS 실행
bfs(graph, v)
print() 