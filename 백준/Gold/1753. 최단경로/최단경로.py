import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for v, w in graph[now]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (distance[v], v))

dijkstra(K)

for i in range(1, V+1):
    print("INF" if distance[i] == INF else distance[i])