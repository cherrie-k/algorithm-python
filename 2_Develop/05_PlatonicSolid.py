'''
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서
나올 수 있는 눈의 합 중 가장 확률이 높은 숫자를 출력하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.

Print the number which is the most likely one to be 
the sum of the eyes, which can be resulted by throwing 
two dice shaped as Platonic Solid which are N-sided and M-sided. 
If there are multiple answers, print them in ascending order.
'''

import sys
#sys.stdin = open("input.txt", "rt")
    
N, M = map(int, input().split())

lst = []
res = set()

for i in range(1, N+1):
    for j in range(1, M+1):
        lst.append(i+j)
        res.add(i+j)

max = 0

for x in res:
    if lst.count(x) > max:
        max = lst.count(x)
        
for y in res:
    if lst.count(y) == max:
        print(y, end = " ")


'''
다른 풀이

import sys
sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
cnt = [0] * (n + m + 3) # cnt는 0으로 초기화된 n+m+3크기의 리스트가 됨. 3은 그냥 좀 넉넉하게 잡아주려고 더함

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1   # 각 합한숫자가 몇번 나왔는지 기록해줌
max = -1
for i in range(n + m + 1):
    if cnt[i] > max:
        max = cnt[i]

for i in range(n + m + 1):
    if cnt[i] == max:
        print(i, end=' ')
        '''