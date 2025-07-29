from collections import deque

def topological_sort_kahn(graph, n):
    # 진입차수 계산
    in_degree = [0] * (n + 1)
    # 1부터 n까지 반복
    for i in range(1, n + 1):
        # 그래프 요소를 반복순회
        for neighbor in graph[i]:
            in_degree[neighbor] += 1
    
    print(f"진입차수: {in_degree}")
    
    # 진입차수가 0인 노드들을 큐에 추가
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    print(f"초기 큐 (진입차수 0): {list(queue)}")
    
    result = []
    step = 1
    
    while queue:
        print(f"\n=== {step}단계 ===")
        print(f"현재 큐: {list(queue)}")
        
        # 진입차수가 0인 노드 처리
        node = queue.popleft()
        result.append(node)
        print(f"처리한 노드: {node}")
        
        # 인접 노드들의 진입차수 감소
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            print(f"노드 {neighbor}의 진입차수: {in_degree[neighbor] + 1} → {in_degree[neighbor]}")
            # 진입차수가 0이 되면 큐에 추가
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                print(f"노드 {neighbor}를 큐에 추가")
        
        print(f"현재 결과: {result}")
        step += 1
    
    # 사이클 검사
    if len(result) != n:
        print(f"사이클 존재! 처리된 노드 수: {len(result)}, 전체 노드 수: {n}")
        return []  # 사이클 존재
    
    return result

if __name__ == "__main__":
    # 테스트 케이스 1: 기본 DAG
    print("=== 테스트 케이스 1: 기본 DAG ===")
    n1 = 5
    graph1 = {
        1: [2, 3],    # 1 → 2, 3
        2: [4, 5],    # 2 → 4, 5
        3: [5],       # 3 → 5
        4: [],        # 4에서 나가는 간선 없음
        5: []         # 5에서 나가는 간선 없음
    }
    
    result1 = topological_sort_kahn(graph1, n1)
    print(f"\n최종 위상정렬 결과: {result1}")
    
    print("\n" + "="*50)
    
    # 테스트 케이스 2: 수강신청 예시
    print("=== 테스트 케이스 2: 수강신청 예시 ===")
    print("1:수학1, 2:수학2, 3:통계학, 4:미적분학, 5:데이터분석")
    n2 = 5
    graph2 = {
        1: [2, 3],    # 수학1 → 수학2, 통계학
        2: [4],       # 수학2 → 미적분학  
        3: [5],       # 통계학 → 데이터분석
        4: [],        # 미적분학
        5: []         # 데이터분석
    }
    
    result2 = topological_sort_kahn(graph2, n2)
    print(f"\n수강 순서: {result2}")
    
    print("\n" + "="*50)
    
    # 테스트 케이스 3: 사이클이 있는 그래프
    print("=== 테스트 케이스 3: 사이클 테스트 ===")
    n3 = 3
    graph3 = {
        1: [2],       # 1 → 2
        2: [3],       # 2 → 3  
        3: [1]        # 3 → 1 (사이클!)
    }
    
    result3 = topological_sort_kahn(graph3, n3)
    if result3:
        print(f"\n위상정렬 결과: {result3}")
    else:
        print("\n위상정렬 불가능 (사이클 존재)") 