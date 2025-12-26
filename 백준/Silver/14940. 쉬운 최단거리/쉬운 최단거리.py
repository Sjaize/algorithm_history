from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
result = [[-1] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    result[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 이미 방문했다면 continue, 방문하지 않았다면 거리 갱신
                if result[nx][ny] != -1: 
                    continue
                else:
                    if board[nx][ny] == 1:
                        result[nx][ny] = result[x][y] + 1
                        queue.append((nx, ny))

# 지도 입력
for _ in range(n):
    board.append(list(map(int, input().split())))

# 거리 계산 (도착 지점에서 역으로 한 번만 수행)
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            result[i][j] = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            bfs(i, j)
            break 
        
# 결과 출력
for row in result:
    print(*row)