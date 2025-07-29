import heapq

class UnionFind:
    """
    크루스칼 알고리즘에서 사용하는 Union-Find (Disjoint Set) 자료구조
    """
    def __init__(self, n):
        self.parent = list(range(n + 1))  # 각 노드의 부모
        self.rank = [0] * (n + 1)         # 트리의 높이
    
    def find(self, x):
        """루트 노드 찾기 (경로 압축 적용)"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """두 집합 합치기"""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # 이미 같은 집합
        
        # rank가 작은 트리를 큰 트리에 붙임
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True

def kruskal_mst(edges, n):
    """
    크루스칼 알고리즘으로 최소 신장 트리 구하기
    
    Args:
        edges: [(가중치, 정점1, 정점2), ...] 형태의 간선 리스트
        n: 정점의 개수
    
    Returns:
        mst_edges: MST를 구성하는 간선들
        total_weight: 총 가중치
    """
    print("=== 크루스칼 알고리즘 ===")
    
    # 간선을 가중치 순으로 정렬
    edges.sort()
    print(f"정렬된 간선들: {edges}")
    
    uf = UnionFind(n)
    mst_edges = []
    total_weight = 0
    
    print("\n단계별 과정:")
    for i, (weight, u, v) in enumerate(edges, 1):
        print(f"{i}단계: 간선 ({u}, {v}), 가중치 {weight}")
        
        # 사이클을 만들지 않으면 선택
        if uf.union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight
            print(f"  → 선택! 현재 총 가중치: {total_weight}")
        else:
            print(f"  → 사이클 생성으로 제외")
        
        # MST 완성 확인
        if len(mst_edges) == n - 1:
            print(f"  → MST 완성! (간선 {n-1}개)")
            break
    
    return mst_edges, total_weight

def prim_mst(graph, start, n):
    """
    프림 알고리즘으로 최소 신장 트리 구하기
    
    Args:
        graph: 인접 리스트 {정점: [(인접정점, 가중치), ...]}
        start: 시작 정점
        n: 정점의 개수
    
    Returns:
        mst_edges: MST를 구성하는 간선들
        total_weight: 총 가중치
    """
    print("=== 프림 알고리즘 ===")
    print(f"시작 정점: {start}")
    
    visited = [False] * (n + 1)
    mst_edges = []
    total_weight = 0
    
    # 우선순위 큐: (가중치, 정점, 이전정점)
    pq = [(0, start, -1)]
    
    step = 1
    
    while pq:
        print(f"\n{step}단계:")
        print(f"우선순위 큐: {pq}")
        
        weight, current, prev = heapq.heappop(pq)
        
        # 이미 방문한 정점이면 건너뜀
        if visited[current]:
            print(f"정점 {current}는 이미 방문됨, 건너뜀")
            continue
        
        # 정점을 MST에 추가
        visited[current] = True
        if prev != -1:  # 시작 정점이 아니면
            mst_edges.append((prev, current, weight))
            total_weight += weight
            print(f"간선 ({prev}, {current}) 선택, 가중치: {weight}")
        else:
            print(f"시작 정점 {current} 선택")
        
        print(f"현재 총 가중치: {total_weight}")
        
        # 인접한 미방문 정점들을 큐에 추가
        for neighbor, edge_weight in graph[current]:
            if not visited[neighbor]:
                heapq.heappush(pq, (edge_weight, neighbor, current))
                print(f"  정점 {neighbor} 큐에 추가 (가중치: {edge_weight})")
        
        step += 1
        
        # MST 완성 확인
        if len(mst_edges) == n - 1:
            print(f"MST 완성! (간선 {n-1}개)")
            break
    
    return mst_edges, total_weight

def edges_to_graph(edges, n):
    """간선 리스트를 인접 리스트로 변환"""
    graph = {i: [] for i in range(1, n + 1)}
    for weight, u, v in edges:
        graph[u].append((v, weight))
        graph[v].append((u, weight))
    return graph

if __name__ == "__main__":
    # 테스트 케이스 1: 기본 예제
    print("=== 테스트 케이스 1: 기본 예제 ===")
    n1 = 4
    edges1 = [
        (1, 1, 2),  # (가중치, 정점1, 정점2)
        (3, 1, 3),
        (3, 1, 4),
        (6, 2, 3),
        (4, 2, 4),
        (2, 3, 4)
    ]
    
    print("원본 그래프:")
    print("1 -- 2 (가중치 1)")
    print("|    |")
    print("|    |")
    print("3 -- 4 (가중치 2)")
    print("가중치: 1-3(3), 1-4(3), 2-3(6), 2-4(4)")
    
    # 크루스칼 알고리즘
    mst1_kruskal, weight1_kruskal = kruskal_mst(edges1.copy(), n1)
    print(f"\n크루스칼 결과:")
    print(f"MST 간선들: {mst1_kruskal}")
    print(f"총 가중치: {weight1_kruskal}")
    
    print("\n" + "="*60)
    
    # 프림 알고리즘 (같은 그래프)
    graph1 = edges_to_graph(edges1, n1)
    mst1_prim, weight1_prim = prim_mst(graph1, 1, n1)
    print(f"\n프림 결과:")
    print(f"MST 간선들: {mst1_prim}")
    print(f"총 가중치: {weight1_prim}")
    
    print("\n" + "="*60)
    
    # 테스트 케이스 2: 복잡한 예제
    print("=== 테스트 케이스 2: 복잡한 예제 ===")
    n2 = 6
    edges2 = [
        (4, 1, 2),
        (4, 1, 3),
        (6, 1, 4),
        (6, 2, 3),
        (3, 2, 5),
        (5, 3, 4),
        (8, 3, 5),
        (2, 3, 6),
        (7, 4, 5),
        (9, 4, 6),
        (1, 5, 6)
    ]
    
    # 크루스칼만 실행 (간단히)
    mst2_kruskal, weight2_kruskal = kruskal_mst(edges2.copy(), n2)
    print(f"\n크루스칼 결과:")
    print(f"MST 간선들: {mst2_kruskal}")
    print(f"총 가중치: {weight2_kruskal}")
    
    print("\n" + "="*60)
    
    # MST의 특성 확인
    print("=== MST의 특성 확인 ===")
    print(f"정점 수: {n2}")
    print(f"MST 간선 수: {len(mst2_kruskal)}")
    print(f"정점 수 - 1 = {n2 - 1}")
    print(f"간선 수가 정점 수 - 1과 같음: {len(mst2_kruskal) == n2 - 1}") 