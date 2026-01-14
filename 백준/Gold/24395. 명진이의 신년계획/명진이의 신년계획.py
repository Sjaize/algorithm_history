import sys
input = sys.stdin.readline

N, M = map(int, input().split())
diseases = [tuple(map(int, input().split())) for _ in range(M)]  # (Ri, Bi, Di)

dp = [[-1] * 51 for _ in range(51)]
dp[0][0] = 0

for Ri, Bi, Di in diseases:
    for r in range(50, Ri-1, -1):
        for b in range(50, Bi-1, -1):
            prev = dp[r - Ri][b - Bi]
            if prev != -1:
                dp[r][b] = max(dp[r][b], prev + Di) 

students = []
for idx in range(1, N+1):
    r, b = map(int, input().split())
    risk = dp[r][b]
    if risk == -1:
        risk = 0
    students.append((risk, idx))

students.sort()  # risk asc, then idx asc

print("\n".join(f"{idx} {risk}" for risk, idx in students))