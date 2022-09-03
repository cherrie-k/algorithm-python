'''
임의의 N개의 숫자가 입력으로 주어집니다. 
N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한 개의 수인 M이 주어지면 
이분 검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는
프로그램을 작성하세요. 단 중복값은 존재하지 않습니다.

A N number of numbers are given as input.
Sort the N numbers in ascending order, 
and then write a program that finds where the number M is, 
which is included in the N numbers. Duplicate values do not exist.
'''

import sys
#sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()

s, e = 0, N - 1
flag = True

while flag:
    mid = (s + e) // 2
    if lst[mid] < M:
        s = mid
    elif lst[mid] > M:
        e = mid
    elif lst[mid] == M:
        print(mid+1)
        flag = False

