# 백준 2110번 - '공유기 설치'

import sys
#sys.stdin = open("input.txt", "rt")

lst = []
n, c = map(int, input().split())
for i in range(n):
    lst.append(int(input()))
    
lst.sort()


min = 1
max = lst[n - 1] - lst[0]

while min <= max:
    mid = (min + max) // 2
    cnt = 1
    cur = lst[0]
    
    for i in lst:
        if i - cur >= mid:
            cur = i
            cnt += 1
    if cnt >= c:
        min = mid + 1
    else:
        max = mid - 1

print(max)