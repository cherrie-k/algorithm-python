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
import sys
#sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
a = list(map(int, input().split()))
# lt는 가장 왼쪽에서부터 가리킴
lt = 0
# rt는 lt의 바로 오른쪽임. 
rt = 1
# tot는 lt부터 rt앞까지의 연속 부분의 합. 이게 m과 같으면 카운트++함.
tot = a[0]  
cnt = 0
while True:
    if tot < m:
        # 목표하는 수보다 작으면 tot를 키워야 함
        if rt < n:
            # rt값을 더해주고,
            tot += a[rt]
            # rt가 가리키는 인덱스를 하나 증가시켜줌
            rt += 1
        else:
            break
    elif tot == m:
        # 목표하는 수와 같아질 때
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        # 목표하는 수보다 커짐 -> 꽝~~
        tot -= a[lt]
        # lt 한칸 증가시킴. 
        lt += 1
print(cnt)
'''