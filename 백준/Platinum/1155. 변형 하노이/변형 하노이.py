# 변형 하노이

import sys
#sys.stdin = open("input.txt", "rt")


N = int(input())                  
lst = list(input().split())

for i in range(6):
    lst[i] = (list(lst[i]))

hanoi = [[[0 for k in range(31)] for j in range(3)] for i in range(3)]
orders = [[0 for j in range(3)] for i in range(6)]


for i in range(0, 6):
    orders[i] = lst[i]
    orders[i][0] = chr(ord(orders[i][0]) - ord('A'))
    orders[i][1] = chr(ord(orders[i][1]) - ord('A'))


for i in range(0, 6):
    start = int(ord(orders[i][0]))
    end = int(ord(orders[i][1]))
    if (not hanoi[start][0][1] and not hanoi[start][1][1] and not hanoi[start][2][1]):
        hanoi[start][end][1] = 1;
        

for i in range(2, N+1):
    for start in range(0, 3):
        for end in range(0, 3):
            if (start != end):
                if (hanoi[start][3-start-end][i-1] and hanoi[3-start-end][end][i-1]):
                    hanoi[start][end][i] = hanoi[start][3-start-end][i-1] + 1 + hanoi[3-start-end][end][i-1]
                elif (hanoi[start][end][i-1] and hanoi[end][start][i-1]):
                    hanoi[start][end][i] = 2 * hanoi[start][end][i-1] + hanoi[end][start][i-1] + 2
                                                 

if hanoi[0][1][N]:
    print(hanoi[0][1][N])
else:
    print(hanoi[0][2][N])


