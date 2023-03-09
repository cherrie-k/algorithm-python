'''
Decision Algorithm

N개의 마구간이 수직선상에 있습니다. 
각 마구간은 x1, x2, x3, ......, xN의 좌표를 가지며, 
마구간간에 좌표가 중복되는 일은 없습니다.
현수는 C마리의 말을 가지고 있는데, 
이 말들은 서로 가까이 있는 것을 좋아하지 않습니다.
각 마구간에는 한 마리의 말만 넣을 수 있고, 
가장 가까운 두 말의 거리가 최대가 되게 말을 마구간에 배치하고 싶습니다.
C마리의 말을 N개의 마구간에 배치했을 때 
가장 가까운 두 말의 거리가 최대가 되는 그 최대값을 구하시오.

There are N number of stables on a vertical line. 
Each stable has coordinates of x1, x2, x3, ......, xN, 
and the stable coordinates do not overlap.
Hyun-soo has C number of horses, which don't like to be close to each other.
Each stable can contain only one horse, 
and he wants to place the horse in the stable so that 
the distance between the two nearest horses is maximum.
Print out the maximum value of the distance between 
the two nearest horses, when C number of horses are placed in N number of stables.
'''


import sys
#sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10**6)

N, C = map(int, input().split()) #  수직선상 마구간 좌표, 말 수
lst = []
largest = 1
for _ in range(N):
    tmp = int(input())
    lst.append(tmp)
    largest = max( largest, tmp)
lst.sort()

'''
어차피 lst.sort() 할거니까 largest 따로 안구하고 hi = lst[N-1]로 해도 됨
'''
    
def countHorse(distance):
    cnt = 1
    base = 0
    for i in range(len(lst)):
        if lst[i]-lst[base] >= distance: # 설정해둔 조건 만족
            cnt += 1
            base = i
        else:
            continue
        '''
        else: continue 없어도 됨
        '''
    return cnt

res = 0
lo, hi = 1, largest

while lo <= hi:
    mid = (lo + hi) // 2  # mid는 가장 가까운 말의 거리
    # 이보다 같거나 커야지 배치 가능하다고 설정. 그렇게 배치 했을 때 cnt가 말의 수와 일치하는지 확인!
    
    if countHorse(mid) < C: # 거리가 너무 좁음
        hi = mid - 1
    else: # 거리가 너무 넓음. 말 수 부족.
        res = mid
        lo = mid + 1

print(res)
    