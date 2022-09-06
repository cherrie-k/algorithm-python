'''
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 
이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+…+A[j-1]+A[j]가 
M이 되는 경우의 수를 구하시오.

There is a sequence  A[1], A[2], …, A[N] of N numerics. 
Calculate the number of cases which the sum of the sequence's
ith value to the jth value, A[i]+A[i+1]+...+A[j-1]+A[j], becomes M.
'''

'''
마지막 조건 시간 제한 exceed 함.
해결해보기!
'''

import sys
#sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
lst = list(map(int, input().split()))


cnt = 0


for i in range(N):
    sum = 0
    for j in range(i, N):
        sum += lst[j]
        if sum == M: 
            cnt += 1
            break
        if sum > M:
            break
    
print(cnt)

'''
'''
import sys
#sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0
while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
print(cnt)