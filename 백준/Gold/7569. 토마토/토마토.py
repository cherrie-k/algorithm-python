import sys
from collections import deque

#sys.stdin = open("input.txt", "rt")

M, N, H = map(int, input().split())

tomato = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

q=deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k]==1:
                q.append((i,j,k))
                
res = 0
while q:
    cnt = len(q)
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1 ,1 ,0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    res += 1
    for _ in range(cnt):
        z, y, x = q.popleft()
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if ( 0 <= nz < H and 0 <= ny < N and 0 <= nx < M 
                and tomato[nz][ny][nx] == 0):
                q.append((nz, ny, nx))
                tomato[nz][ny][nx] = 1
            else:
                continue
            
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 0:
                print(-1)
                exit(0)
                
print(res - 1)