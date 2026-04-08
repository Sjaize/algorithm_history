from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

def dfs(v, visited):
    visited[v] = True
    print(v, end = " ")

    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)

def bfs(v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        x = queue.popleft()
        print(x, end = " ")
        for i in graph[x]:

            if not visited[i]:
                visited[i] = True
                queue.append(i)

visited = [False] * (N+1)
dfs(V, visited)
print()
visited = [False] * (N+1)
bfs(V, visited)