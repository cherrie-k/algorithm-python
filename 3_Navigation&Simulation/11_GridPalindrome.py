'''
1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 
격자판 위에서 가로방향 또는 세로방향으로 길이 5자리 회문수가 
몇 개 있는지 구하는 프로그램을 작성하세요.
회문수란 121과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수를 말합니다.

Given a 7*7 grid filled with positive integers from 1 to 9, 
write a program to determine how many 5-digit palindrome numbers are in 
the grid either horizontally or vertically.
Palindrome number means a number is read the same backward and forward, 
such as the number 121.

2 4 1 5 3 2 6   --> number of palindrome #s: 3
3 5 1 8 7 1 7       1. (1 2 3 2 1) (hori-)   
8 3 2 7 1 3 8       2. (2 2 1 2 2) (vert-)
6 1 2 3 2 1 1       3. (2 5 6 5 2) (hori-)
1 3 1 3 5 3 2
1 1 2 5 6 5 2
1 2 2 2 2 1 5
''' 

import sys
#sys.stdin = open("input.txt", "rt")

lst = [list(map(int, input().split())) for _ in range(7)] 

cnt = 0
# 가로 검사(horizontal)
for i in range(7):
    for j in range(3):  #5개만 확인하기 위해서
        for k in range(2):
            if lst[i][j+k] != lst[i][j+4-k]:
                break
        else:
            cnt += 1
# 세로 검사(vertical)            
for j in range(7):
    for i in range(3):  #5개만 확인하기 위해서
        for k in range(2):
            if lst[i+k][j] != lst[i+4-k][j]:
                break
        else:
            cnt += 1        

print(cnt)



''' 
다른 풀이
import sys
#sys.stdin = open("input.txt", "rt")
board = [list(map(int, input().split())) for _ in range(7)] 
cnt = 0

for i in range(3):   #5개만 확인하기 위해서
    for j in range(7): 
        # slice 기능 사용
        tmp = board[j][i:i+5]  # 0부터 4까지, 5개 분리해냄. 
        # slice 해낸게 회문인지 확인
        if tmp == tmp[::-1]: 
            cnt += 1
        
        # 길이 5면 5/2 해서 2 바퀴만 검사하면 회문 판별 가능.
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break   # 회문이 아니니 break
        else: # break 안당하고 끝남. 즉 회문임. 
            cnt += 1       

print(cnt)
'''
