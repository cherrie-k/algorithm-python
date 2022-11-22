import sys
from itertools import combinations

#sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))
    
# 바이러스 전파하는 함수
def virus(tmp, x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        if 0<=xx<N and 0<=yy<M and tmp[xx][yy] == 0:
            tmp[xx][yy] = 2
            virus(tmp, xx, yy)

# 0 인 칸 수 세기
def countZero(tmp):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 0:
                cnt += 1
    return cnt



result = 0
tmp = [[0]*M for _ in range(N)]

# 빈 칸의 좌표 구하기
zeroIndex = []
for i in range(N):
    for j in range(M):
        if lst[i][j] == 0:
            zeroIndex.append((i, j))
                        
for coordinates in list(combinations(zeroIndex, 3)):
    # 3개의 빈 벽에 벽을 설치
    for coordinate in coordinates:
        x, y = coordinate
        lst[x][y] = 1
    #바이러스를 전파시킬 임시 연구소 생성(2d배열)
    for i in range(N):
        for j in range(M):
            tmp[i][j] = lst[i][j]
    #바이러스 감염
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                virus(tmp, i, j)
    result = max(result, countZero(tmp))
    
    #설치한 벽 제거
    for coordinate in coordinates:
        x, y = coordinate
        lst[x][y] = 0
        
print(result)

