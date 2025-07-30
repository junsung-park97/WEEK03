# 어느 정점에서 시작해서 끝까지 dfs로 탐색하고 탐색된 노드들을 출력하는것.
import sys

sys.setrecursionlimit(1000)
input = sys.stdin.readline

def dfs (node):
    visited[node] = True
    if visited[node] == True:
        result.append(visited[node])

    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)

nodes = int(input())
edge = int(input())
graph = [[] for _ in range(nodes + 1)]
visited = [False] * (nodes + 1)
result = []

for _ in range(edge):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(1)

print(len(result) - 1)




