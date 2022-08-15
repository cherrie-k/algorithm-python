'''
1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 
다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다.
규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다.
규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.

예를 들어, 3개의 눈 3, 3, 6이 주어지면 
상금은 1,000+3*100으로 계산되어 1,300원을 받게 된다. 
또 3개의 눈이 2, 2, 2로 주어지면 
10,000+2*1,000 으로 계산되어 12,000원을 받게 된다.
3개의 눈이 6, 2, 5로 주어지면 그 중 가장 큰 값이 6이므로 
6*100으로 계산되어 600원을 상금으로 받게 된다.
N 명이 주사위 게임에 참여하였을 때, 
가장 많은 상금을 받은 사람의 상금을 출력하시오.

There is a game in which you throw three dice with eyes from 1 to 6 
and receive a prize according to the following rules.
Rule (1) If you have the same three eyes, 
you will receive a prize of 10,000₩ + (same eye)*1,000₩.
Rule (2) If only two eyes are the same, 
you will receive a prize of 1,000₩ + (same eye)*100₩.
Rule (3) If all eyes are different, 
you will receive a prize of (The biggest eye)*100₩.

For example, given three eyes 3, 3, and 6, 
the prize will be calculated as 1,000+3*100 and receive 1,300₩.
If eyes are given as 2, 2, and 2,
it will be calculated as 10,000+2*1,000 and will receive 12,000₩.
If three eyes are given 6, 2, and 5, the largest value is 6, 
so it's calculated as 6*100 and 600 won will be awarded.
N number of people and their dice result will be given, 
so print out the prize of the person who received the most money.
'''

import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())
maxPrize = 0

lst = []

for n in range(N):
    a, b, c = map(int, input().split())
    max = 0
    for i in range(3):
        if i > max:
            max = i
    if (a == b == c):
        val = 10000 + a * 1000
    elif (a == b) and (a != c):
        val = 1000 + a * 100
    elif (a == c) and (a != b):
        val = 1000 + a * 100
    elif (b == c) and (b != a):
        val = 1000 + b * 100
    else:
        val =  max * 600
    lst.append(val)

lst.sort()
print(lst[N-1])    

