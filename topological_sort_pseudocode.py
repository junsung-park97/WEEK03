from collections import deque

def topological_sort_kahn_pseudocode(graph, n):
    """
    Kahn 알고리즘 슈도코드를 따른 구현
    """
    print("=== Kahn 알고리즘 (슈도코드 기반) ===")
    
    # 1-2: 진입차수 배열 초기화
    in_degree = [0] * (n + 1)
    
    # 4-6: 진입차수 계산
    for u in range(1, n + 1):
        for v in graph[u]:
            in_degree[v] = in_degree[v] + 1
    
    print(f"진입차수: {in_degree}")
    
    # 8-11: 진입차수 0인 정점들을 큐에 추가
    Q = deque()
    for v in range(1, n + 1):
        if in_degree[v] == 0:
            Q.append(v)
    
    print(f"초기 큐: {list(Q)}")
    
    # 13: 결과 리스트 초기화
    result = []
    
    # 14: 큐가 비지 않을 때까지 반복
    step = 1
    while Q:
        print(f"\n{step}단계:")
        print(f"현재 큐: {list(Q)}")
        
        # 15: 큐에서 정점 제거
        u = Q.popleft()
        
        # 16: 결과에 추가
        result.append(u)
        print(f"정점 {u} 처리")
        
        # 18-21: 인접 정점들의 진입차수 감소
        for v in graph[u]:
            in_degree[v] = in_degree[v] - 1
            print(f"  정점 {v}의 진입차수: {in_degree[v] + 1} → {in_degree[v]}")
            
            if in_degree[v] == 0:
                Q.append(v)
                print(f"  정점 {v}를 큐에 추가")
        
        print(f"현재 결과: {result}")
        step += 1
    
    # 23-26: 사이클 검사
    if len(result) != n:
        print(f"사이클 존재! 처리된 정점: {len(result)}, 전체 정점: {n}")
        return "CYCLE_EXISTS"
    else:
        return result

def topological_sort_dfs_pseudocode(graph, n):
    """
    DFS 기반 위상정렬 슈도코드를 따른 구현
    """
    print("=== DFS 기반 위상정렬 (슈도코드 기반) ===")
    
    # 색깔 정의
    WHITE, GRAY, BLACK = 0, 1, 2
    
    # 1-3: 초기화
    color = [WHITE] * (n + 1)
    predecessor = [-1] * (n + 1)
    
    # 5: 결과 리스트 초기화
    result = []
    
    def dfs_visit(u):
        """DFS_VISIT 함수"""
        print(f"  DFS_VISIT({u}) 시작")
        
        # 1: 방문 중으로 표시
        color[u] = GRAY
        print(f"    정점 {u}를 GRAY로 표시")
        
        # 3-8: 인접 정점들 확인
        for v in graph[u]:
            print(f"    인접 정점 {v} 확인")
            
            # 4-5: 사이클 검사
            if color[v] == GRAY:
                print(f"    사이클 발견! {u} → {v}")
                return False
            
            # 6-8: 미방문 정점 재귀 호출
            if color[v] == WHITE:
                if not dfs_visit(v):
                    return False
        
        # 10: 완료 표시
        color[u] = BLACK
        print(f"    정점 {u}를 BLACK으로 표시")
        
        # 11: 결과에 추가 (완료 순서)
        result.insert(0, u)  # 앞에 추가
        print(f"    정점 {u}를 결과 앞에 추가: {result}")
        
        return True
    
    # 7-10: 모든 정점에서 DFS 시작
    for u in range(1, n + 1):
        if color[u] == WHITE:
            print(f"\n정점 {u}에서 DFS 시작")
            if not dfs_visit(u):
                return "CYCLE_EXISTS"
    
    # 12: 결과 반환 (이미 역순으로 구성됨)
    return result

def compare_algorithms(graph, n):
    """두 알고리즘 결과 비교"""
    print("=== 알고리즘 비교 ===")
    
    # Kahn 알고리즘
    result_kahn = topological_sort_kahn_pseudocode(graph.copy(), n)
    
    print("\n" + "="*50)
    
    # DFS 기반 알고리즘  
    result_dfs = topological_sort_dfs_pseudocode(graph.copy(), n)
    
    print("\n" + "="*50)
    
    print("=== 결과 비교 ===")
    print(f"Kahn 결과:     {result_kahn}")
    print(f"DFS 결과:      {result_dfs}")
    
    if result_kahn != "CYCLE_EXISTS" and result_dfs != "CYCLE_EXISTS":
        print(f"결과 동일:     {result_kahn == result_dfs}")
        print("(위상정렬 결과는 여러 개가 가능하므로 다를 수 있습니다)")

if __name__ == "__main__":
    # 테스트 케이스 1: 기본 DAG
    print("=== 테스트 케이스 1: 기본 DAG ===")
    n1 = 5
    graph1 = {
        1: [2, 3],
        2: [4, 5],
        3: [5],
        4: [],
        5: []
    }
    
    print("그래프 구조:")
    print("1 → 2, 3")
    print("2 → 4, 5") 
    print("3 → 5")
    print("4 → (없음)")
    print("5 → (없음)")
    
    compare_algorithms(graph1, n1)
    
    print("\n" + "="*70)
    
    # 테스트 케이스 2: 사이클이 있는 그래프
    print("=== 테스트 케이스 2: 사이클 테스트 ===")
    n2 = 3
    graph2 = {
        1: [2],
        2: [3],
        3: [1]  # 사이클!
    }
    
    print("그래프 구조 (사이클):")
    print("1 → 2")
    print("2 → 3")
    print("3 → 1 (사이클!)")
    
    compare_algorithms(graph2, n2) 