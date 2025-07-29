import heapq

def dijkstra(graph, start, n):
    """
    다익스트라 알고리즘으로 최단 거리 계산
    
    Args:
        graph: 인접 리스트 {정점: [(인접정점, 가중치), ...]}
        start: 시작 정점
        n: 정점의 개수
    
    Returns:
        distance: 시작 정점에서 각 정점까지의 최단 거리 리스트
    """
    # 거리 배열 초기화
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    
    # 우선순위 큐 (거리, 정점)
    pq = [(0, start)]
    
    print(f"시작 정점: {start}")
    print(f"초기 거리: {distance}")
    
    step = 1
    
    while pq:
        print(f"\n=== {step}단계 ===")
        print(f"우선순위 큐: {pq}")
        
        # 가장 가까운 정점 선택
        current_dist, current_node = heapq.heappop(pq)
        
        print(f"선택된 정점: {current_node}, 거리: {current_dist}")
        
        # 이미 처리된 정점이면 건너뜀
        if current_dist > distance[current_node]:
            print(f"정점 {current_node}는 이미 처리됨, 건너뜀")
            continue
        
        # 인접한 정점들 확인
        for neighbor, weight in graph[current_node]:
            new_dist = current_dist + weight
            print(f"  정점 {neighbor}: 현재 거리 {distance[neighbor]}, 새 거리 {new_dist}")
            
            # 더 짧은 경로를 발견하면 업데이트
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
                print(f"    → 업데이트! 거리: {new_dist}")
            else:
                print(f"    → 업데이트 안 함")
        
        print(f"현재 거리 배열: {distance}")
        step += 1
    
    return distance

def dijkstra_with_path(graph, start, n):
    """
    경로 추적이 가능한 다익스트라 알고리즘
    """
    distance = [float('inf')] * (n + 1)
    previous = [-1] * (n + 1)  # 이전 정점 추적
    distance[start] = 0
    
    pq = [(0, start)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_dist > distance[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            new_dist = current_dist + weight
            
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                previous[neighbor] = current_node  # 이전 정점 기록
                heapq.heappush(pq, (new_dist, neighbor))
    
    return distance, previous

def get_path(previous, start, end):
    """
    시작점에서 끝점까지의 경로 복원
    """
    path = []
    current = end
    
    while current != -1:
        path.append(current)
        current = previous[current]
    
    path.reverse()
    
    # 경로가 시작점에서 시작하지 않으면 연결되지 않음
    if path[0] != start:
        return []
    
    return path

if __name__ == "__main__":
    # 테스트 케이스 1: 기본 예제
    print("=== 테스트 케이스 1: 기본 다익스트라 ===")
    n1 = 4
    graph1 = {
        1: [(2, 4), (3, 2), (4, 7)],
        2: [(1, 4), (3, 1)],
        3: [(1, 2), (2, 1), (4, 3)],
        4: [(1, 7), (3, 3)]
    }
    
    result1 = dijkstra(graph1, 1, n1)
    print(f"\n최종 최단 거리: {result1[1:]}")
    
    print("\n" + "="*50)
    
    # 테스트 케이스 2: 경로 추적
    print("=== 테스트 케이스 2: 경로 추적 ===")
    distance2, previous2 = dijkstra_with_path(graph1, 1, n1)
    
    print(f"최단 거리: {distance2[1:]}")
    print(f"이전 정점: {previous2[1:]}")
    
    # 각 정점까지의 경로 출력
    for end in range(1, n1 + 1):
        if distance2[end] != float('inf'):
            path = get_path(previous2, 1, end)
            print(f"정점 1 → 정점 {end}: 경로 {path}, 거리 {distance2[end]}")
    
    print("\n" + "="*50)
    
    # 테스트 케이스 3: 연결되지 않은 그래프
    print("=== 테스트 케이스 3: 연결되지 않은 그래프 ===")
    n3 = 5
    graph3 = {
        1: [(2, 3)],
        2: [(3, 4)],
        3: [],
        4: [(5, 2)],  # 1,2,3과 연결되지 않음
        5: []
    }
    
    result3 = dijkstra(graph3, 1, n3)
    print(f"\n최단 거리: {result3[1:]}")
    print("inf는 연결되지 않은 정점을 의미합니다.") 