# dp[mask][i] = (mask 집합의 도시들을 방문하고 i에 도착한 최소 비용)
import sys
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

INF = int(1e9)
FULL = (1 << N) - 1

dp = [[INF] * N for _ in range(1 << N)]

dp[1][0] = 0

for mask in range(1 << N):
    for u in range(N):
        if not (mask & (1 << u)):
            continue
        if dp[mask][u] == INF:
            continue
        
        for v in range(N):
            if mask & (1 << v):
                continue
            if W[u][v] == 0:
                continue
            next_mask = mask | (1 << v)
            dp[next_mask][v] = min(dp[next_mask][v], dp[mask][u] + W[u][v])

answer = INF
for i in range(N):
    if W[i][0] == 0:
        continue
    answer = min(answer, dp[FULL][i] + W[i][0])

print(answer)