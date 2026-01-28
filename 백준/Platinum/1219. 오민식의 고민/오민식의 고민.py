from collections import deque
import sys

input = sys.stdin.readline
INF = -int(1e9)

def bfs(start, end):
    visited = [False] * N
    q = deque([start])
    visited[start] = True

    while q:
        node = q.popleft()
        if node == end:
            return True
        for u, v, w in edges:
            if u == node:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
    return False

# 벨만 포드 알고리즘
def bellmanFord(start, end):
    # testcase 5번에 따르면, 시작 지점의 benefit은 시작하자마자 얻어져야 함.
    distance[start] = benefits[start]

    for i in range(N-1):
        for u, v, w in edges:
            if distance[u] != INF and distance[u] + w > distance[v]:
                distance[v] = distance[u] + w

    if distance[end] == INF:
        return "gg"
    
    for u, v, w in edges:
        if distance[u] != INF and distance[u] + w > distance[v]:
            if bfs(v, end):
                return "Gee"
            
    return distance[end]

# 입력 및 전처리
N, start, end, M = map(int, input().split())

distance = [INF] * N
edges = []

for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append([u,v,-w])

benefits = list(map(int, input().split()))

for edge in edges:
    edge[2] += benefits[edge[1]]

# 결과 출력
print(bellmanFord(start, end))