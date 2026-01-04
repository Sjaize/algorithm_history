import math
N, K = map(int, input().split())
print(math.comb(N+K-1, N) % 1000000000)