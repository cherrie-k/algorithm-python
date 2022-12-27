'''
지도 정보가 N*N 격자판에 주어집니다. 
각 격자에는 그 지역의 높이가 쓰여있습니다. 
각 격자판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 
봉우리 지역입니다. 봉우리 지역이 몇 개 있는지 알아내는 프로그램을 작성하세요.
격자의 가장자리는 0으로 초기화 되었다고 가정합니다.
만약 N=5 이고, 격자판의 숫자가 다음과 같다면 봉우리의 개수는 10개입니다.
    0 0 0 0 0 0 0
    0 5 3 7 2 3 0
    0 3 7 1 6 1 0
    0 7 2 5 3 4 0
    0 4 3 6 4 1 0
    0 8 7 3 5 2 0
    0 0 0 0 0 0 0
Map information is given as a N*N grid. 
Each grid shows the height of the area. 
If the number on each grid that is greater than its surroundings,
which includes top, bottom, left, and right, is the peak area. 
Write a program to find out how many peak areas there are.
Assume that the edge of the grid is initialized with 0.
If N = 5, and the number of grid plates is equal to the grid above, 
then the number of peaks is 10.
'''

import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)] 

for i in range(N):
    lst[i].insert(0, 0)
    lst[i].append(0)
lst.insert(0, [0] * (N + 2))
lst.append([0] * (N + 2))
   
def isPeak(area, a, b):
    if area[a][b] <= area[a - 1][b]:
        return False
    elif area[a][b] <= area[a + 1][b]:
        return False
    elif area[a][b] <= area[a][b - 1]:
        return False
    elif area[a][b] <= area[a][b + 1]:
        return False
    return True
         
cnt = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
       if isPeak(lst, i, j):
           cnt += 1

print(cnt)

'''
다른 풀이

import sys
#sys.stdin = open("input.txt", "rt")
dx = [-1, 0, 1, 0]  # 상하좌우 탐색하게하는 리스트
dy = [0, 1, 0, -1]  # 상하좌우 탐색하게하는 리스트
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)] 
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)
# 여기까지 똑같

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        # all 함수는 모든 조건이 참이 돼야 참이 됨
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)): 
            # i+dx[k]가 행, j+dy[k]가 열 검사해줌. 4번 상하좌우 돌면서 검사해줌. 
            cnt += 1

print(cnt)
'''
