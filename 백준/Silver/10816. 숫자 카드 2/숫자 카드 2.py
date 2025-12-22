import sys
input = sys.stdin.readline

d = {}

N = int(input())
for x in map(int, input().split()):
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

M = int(input())
for x in map(int, input().split()):
    if x in d:
        print(d[x], end= " ")
    else:
        print(0, end = " ")