# 분기한정법으로 풀까, DP로 풀까 고민했습니다. 
# 분기한정법으로 풀어본 분 계시면 공유해주세요.

import sys
input = sys.stdin.readline

memo = {}

N, M, H = map(int, input().split())

table = [[0] for _ in range(N+1)]

for i in range(1, N+1):
    table[i].extend(map(int, input().split()))

# n is current player, and n is current height.
def building(n, h):
    if (n, h) in memo:
        return memo[(n, h)]
    
    if n == N:
        return 1 if h == H else 0
    
    result = 0
    for block in table[n+1]:
        if (h + block) <= H:
            result = (result + building(n+1, h+block)) % 10007

    memo[(n, h)] = result
    return result

print(building(0, 0))