'''
오름차순으로 정렬이 된 두 리스트가 주어지면 
두 리스트를 오름차순으로 합쳐 출력하세요.

Given two lists sorted in ascending order, 
combine the two lists in ascending order and print the result.
'''

import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())
l1 = list(map(int, input().split()))
M = int(input())
l2 = list(map(int, input().split()))


'''
방법1: '+'를 이용한 방법

l1 = l1 + l2
l1.sort()
for i in l1:
    print(i, end=' ')
'''

'''
방법2: .extend(~) 함수를 이용한 방법
'''
l1.extend(l2)
l1.sort()
for i in l1:
    print(i, end=' ')
    

'''
다른 풀이
sort를 이용하면 시간복잡도가 NlogN이 된다!
N짜리 시간복잡도로 구현해보자~~

두 리스트에 포인터 각각 한개씩 가장 앞에 배치.

import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

p1=p2=0
c=[]
while p1<n and p2<m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
if p1<n:
    c = c+a[p1:]
if p2<m:
    c = c+b[p2:]
for x in c:
    print(x, end=' ')
        
'''