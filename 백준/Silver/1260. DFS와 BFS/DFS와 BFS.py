from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 노드 방문 순서 정렬
for i in range(N+1):
    graph[i].sort()

def dfs(v, visited):
    visited[v] = True
    print(v, end = " ")
    for node in graph[v]:
        if not visited[node]:
            dfs(node, visited)

def bfs(v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        cur = queue.popleft()
        print(cur, end = " ")

        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

# 결과 출력
visited = [False] * (N+1)
dfs(V, visited)
print()

visited = [False] * (N+1)
bfs(V, visited)