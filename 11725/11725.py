import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
parent = [0] * (n + 1)

for _ in range(n - 1):
    v, u = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)

def dfs(node):
    visited[node] = True
    for adj in graph[node]:
        if not visited[adj]:
            parent[adj] = node
            dfs(adj)

dfs(1)

for i in range(2, n + 1):
    print(parent[i])

