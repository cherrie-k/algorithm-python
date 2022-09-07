'''
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 
두 대각선의 합 중 가장 큰 합을 출력하세요.

Given a grid of N*N, calculate the sum of each row, 
the sum of each column, and the sum of two longest diagonal lines.
Print the largest sum.
'''

import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())
lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))

max = 0

# 행 더함
for i in range(N):
    sum = 0
    for j in range(N):
        sum += lst[j][i]
    if sum > max:
        max = sum;

# 열 더함
for i in range(N):
    sum = 0
    for j in range(N):
        sum += lst[i][j]
    if sum > max:
        max = sum;

# 좌측 상단에서 우측 하단으로 가는 대각선
sum = 0
for i in range(N):
    sum += lst[i][i]
if sum > max:
    max = sum
 
# 우측 상단에서 좌측 하단으로 가는 대각선       
sum = 0       
for i in range(N):
    sum += lst[i][N - i - 1]
if sum > max:
    max = sum


print(max)


'''
다른 풀이
import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

largest = -2147000000

# 행과 열 합 한번에 구하기
for i in range(n):  
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]    # j를 고정하고 i를 돌림
        sum2 += a[j][i]    # i로 열이 고정되고 j가 돈다
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

# 대각선 합도 한번에 구하기
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n - i - 1]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2

print(largest)
'''