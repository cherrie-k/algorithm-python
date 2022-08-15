'''
두 개의 자연수 N과 K가 주어졌을 때, 
N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을
작성하시오.
Given two natural numbers N and K, 
write a program that prints the Kth smallest number 
among the divisors of N.
'''

'''
#import sys
#sys.stdin = open("input.txt", "rt")
#n, k=map(int, input().split())

n = int(input("input N: "))
k = int(input("input K: "))
l = []

for i in range(1, n+1):
    if n % i == 0:
        l.append(i)

if(k <= len(l)):
    print(l[k-1])
else:
    print(-1)
''' 
    


n = int(input("input N: "))
k = int(input("input K: ")) 
cnt = 0

for i in range(1, n+1):
    if n%i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
#정상적으로 끝나지 못해서 break가 안 걸린 경우 else로 옴
else:
    print(-1)
