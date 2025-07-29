from collections import deque

def detailed_bfs(graph, start):
    visited = set()           # 방문한 노드들
    queue = deque([start])    # 탐색할 노드들의 큐
    result = []               # 방문 순서
    
    print(f"시작 노드: {start}")
    step = 1
    
    while queue:
        print(f"\n=== {step}단계 ===")
        print(f"현재 큐: {list(queue)}")
        
        # 큐에서 노드를 하나 꺼냄
        current = queue.popleft()
        print(f"처리할 노드: {current}")
        
        # 이미 방문한 노드라면 건너뜀
        if current in visited:
            print(f"{current}는 이미 방문됨, 건너뜀")
            continue
            
        # 노드 방문 처리
        visited.add(current)
        result.append(current)
        print(f"{current} 방문 완료")
        
        # 인접한 미방문 노드들을 큐에 추가
        neighbors = []
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                neighbors.append(neighbor)
        
        if neighbors:
            print(f"큐에 추가된 노드들: {neighbors}")
        else:
            print("추가할 노드 없음")
            
        print(f"방문 순서: {result}")
        step += 1
    
    return result