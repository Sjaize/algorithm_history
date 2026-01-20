import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

q = [(0, 0)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = -1

while q:
    _q = [] # 다음에 둘 곳
    while q:
        x, y = q.pop()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                v = arr[nx][ny]
                if v < 0: # 이미 방문
                    continue
                elif not v: # 빈 자리
                    arr[nx][ny] = -1
                    q.append((nx, ny))
                elif v == 1: # 치즈
                    arr[nx][ny] += 1
                else: # v > 1, 한 번 방문했는데 재방문
                    arr[nx][ny] = -1
                    _q.append((nx, ny)) # 다음 turn(한 시간 후) 방문
    q = _q
    ans += 1

print(ans)