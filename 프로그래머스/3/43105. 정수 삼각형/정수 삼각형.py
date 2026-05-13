def solution(triangle):
    n = len(triangle[-1])
    d = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i+1):
            d[i][j] = triangle[i][j]
    
    for i in range(n): 
        for j in range(n):
            if i-1 < 0:
                continue
            if j-1 < 0:
                d[i][j] = d[i][j] + d[i-1][j]
            else:
                d[i][j] += max(d[i-1][j-1], d[i-1][j])
    
    return max(d[-1])