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