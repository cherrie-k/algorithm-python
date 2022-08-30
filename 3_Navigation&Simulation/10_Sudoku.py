'''
스도쿠는 매우 간단한 숫자 퍼즐이다. 
9×9 크기의 보드가 있을 때, 각 행과 각 열, 그리고 9개의 3×3 크기의 보드에 
1부터 9까지의 숫자가 중복 없이 나타나도록 보드를 채우면 된다.
완성된 9×9 크기의 수도쿠가 정확하게 풀어진 것이면 “YES", 
잘 못 풀었으면 ”NO"를 출력하세요.

Sudoku is a very simple numeric puzzle. 
When there is a board of size 9×9, the board should be filled in 
such a way that each row, each column, and nine 3×3 boards 
are filled with numbers from 1 to 9 without overlapping.
Print out "YES" if the given 9x9 size Sudoku is solved correctly, 
and "NO" if it is not solved correctly.
'''


import sys
#sys.stdin = open("input.txt", "rt")

lst = [list(map(int, input().split())) for _ in range(9)] 


def sudoku(board):
    for i in range(9):     # 가로줄 검사
        tmp = []
        for j in range(9):
            if board[i][j] not in tmp:
                tmp.append(board[i][j])
            else:
                return False
    for i in range(9):  # 세로줄 검사
        tmp = []
        for j in range(9):
            if board[j][i] not in tmp:
                tmp.append(board[j][i])
            else: 
                return False
    for i in range(0, 8, 3):    # 3X3 검사
        for j in range(0, 8, 3):
            tmp = []
            for a in range(3):
                for b in range(3):
                    if board[i+a][j+b] not in tmp:
                        tmp.append(board[i+a][j+b])
                    else:
                        return False
    return True
        

if sudoku(lst) is True:
    print("YES")
else:
    print("NO")