'''
채리는 곳감을 만들기 위해 감을 깎아 마당에 말리고 있습니다. 
채리의 마당은 N*N 격자판으로 이루어져 있으며, 
채리는 각 격자단위로 말리는 감의 수를 정합니다.
그런데 해의 위치에 따라 특정 위치의 감은 잘 마르지 않습니다. 
그래서 채리는 격자의 행을 기준으로 왼쪽, 또는 오른쪽으로 회전시켜 
위치를 변경해 모든 감이 잘 마르게 합니다.
만약 회전명령 정보가 2 0 3이면 2번째 행을 왼쪽으로 3만큼 
아래 그림처럼 회전시키는 명령입니다.
(전: 2행: | 12 | 39 | 30 | 23 | 11 |)
(후: 2행: | 23 | 11 | 12 | 39 | 30 |)
첫 번째 수는 행번호, 두 번째 수는 방향인데 0이면 왼쪽, 1이면 오른쪽이고, 
세 번째 수는 회전하는 격자의 수입니다.
M개의 회전명령을 실행하고 난 후 마당의 모래시계 모양의 영역에는 
감이 총 몇개가 있는지 출력하는 프로그램을 작성하세요.

Cherrie peels persimmons and dries them in the yard to make 
dried persimmon chips. Cherrie's yard is the form of an N*N grid, 
and the number in grid determines the number of persimmons in each grid.
However, depending on the location of the sun, 
persimmons at certain locations do not dry well. 
So based on the row of the grid, rotate the grid left or right 
to change its position so that all persimmons dry well.
If the rotation command is 2 0 3, 
it means to rotate the second row, 3 times to the left, as shown below.
(Before: row 2: | 12 | 39 | 30 | 23 | 11 |)
(After : row 2: | 23 | 11 | 12 | 39 | 30 |)
In the input command, The first number is row number, 
the second number is direction(0 for left, 1 for right), 
and the third number is the number of rotation of the grid.
After executing M rotation commands, 
Print out how many persimmons are in the hourglass shaped area of the yard.
'''


import sys
#sys.stdin = open("input.txt", "rt")

lst = []

N = int(input())
for i in range(N):
    lst.append(list(map(int, input().split())))
M = int(input())

# ratate grids
for i in range(M):
    row, dire, times = map(int, input().split())
    if dire == 1:  # right
        for j in range(times):
            tmp = lst[row-1].pop()
            lst[row-1].insert(0, tmp)
    elif dire == 0: #left
        for j in range(times):
            tmp = lst[row-1].pop(0)
            lst[row-1].append(tmp)
        
s, e = 0, N
sum = 0
for i in range(N):
    for j in range(s, e):
        sum += lst[i][j]
    if i < N//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(sum)


