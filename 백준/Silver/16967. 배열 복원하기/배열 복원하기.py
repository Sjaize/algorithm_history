import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().split())

A = [[0] * W for _ in range(H)]
B = []

# 행렬 B 입력
for _ in range(H+X):
    row = list(map(int, input().split()))
    B.append(row)

# 행렬 A 계산
for i in range(H):
    for j in range(W):
        B[i+X][j+Y] -= B[i][j]
        A[i][j] = B[i][j]

for row in A:
    print(*row)