from collections import deque
import sys
input = sys.stdin.readline

# 입력, O(N * M)
N, M = map(int, input().split())

total = 0
board = []

for i in range(N):
    board.append(list(map(int, input().split())))
    total = total + sum(board[i])

# test1: print(total) print(board[N-1][M-1])

# 외부 공기 구분, O(N * M)
def spread():
    visited = [[False] * M for _ in range(N)]
    queue = deque([(0,0)])
    visited[0][0] = True

    while queue:
        r, c = queue.popleft()
        board[r][c] = -1
        for nr, nc in (r-1,c), (r+1,c), (r,c-1), (r,c+1):
            if (0 <= nr < N) and (0 <= nc < M):
                if board[nr][nc] != 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

# test2: spread() print(board)

# 녹을 치즈 구분 (상수)
def is_valid(r, c):
    count = 0
    for nr, nc in (r-1,c), (r+1,c), (r,c-1), (r,c+1):
        if board[nr][nc] == -1:
            count = count + 1
    
    if count >= 2:
        return True

    return False

# 결과 계산, O()
time = 0

while True:
    spread()

    melt = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                if is_valid(i,j):
                    melt.append((i,j))

    for r, c in melt:
        board[r][c] = -1
        total = total - 1

    time = time + 1
    if total == 0:
        print(time)
        break