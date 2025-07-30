from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

def topological_sort(n, graph):
    in_degree = [0] * (n + 1)
    # 그래프리스트의 전체 노드 반복
    for node in range(1, n + 1):
        #그래프중에서 위의 for문의 반복변수에 해당하는 요소와 인접된 노드들을 반복
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque([])
    #그래프리스트의 전체 노드 반복 => 인접차수 반복아닌가?
    for node in range(1, n + 1):
        if neighbor == 0:
            queue.append(node)
    result = []
    #queue의 요소가 없어질때까지 반복
    while queue:
        node = queue.popleft()
        # 그래프에서 pop된 요소의 인접 노드들을 반복
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                result.append(neighbor)
            
    if len(result) != n:
        print('사이클이 존재합니다')
    else:
        return print(result)
