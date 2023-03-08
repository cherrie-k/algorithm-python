'''
엘리트 학원은 자체적으로 K개의 랜선을 가지고 있다. 
그러나 K개의 랜선은 길이가 제각각이다. 선생님은 랜선을 
모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다. 
예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm 은 버려야 한다. (이미 자른 랜선은 붙일 수 없다.)
편의를 위해 랜선을 자를때 손실되는 길이는 없다고 가정하며, 
기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자. 
그리고 자를 때는 항상 센티미터 단위로 정수 길이만큼 자른다고 가정하자. 
N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 
이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.

A company has K number of LAN cables.
However, the K number of LAN cables vary in length. 
A worker wanted to make all the LAN cables into N number of LAN cables
which are all the same in length, so he had to cut the K number of LAN cables.
For example, if you cut two 140cm LAN cables from a 300cm LAN cable, 
you should throw away 20cm. (You cannot attach an already cut LAN cable.) 
For convenience, assume that there is no lost length when cutting the LAN cables, 
and that there is no case where N number of LAN cables cannot be made with 
existing K number of LAN lines. Also, when you cut it, 
suppose you always cut it by an integer length in centimeters.
Making more than N is also included in making N.
Write a program to find the maximum length of LAN cable you can make.
'''

import sys
#sys.stdin = open("input.txt", "rt")

K, N = map(int, input().split())
lst = []
largest = 1
for _ in range(K):
    tmp = int(input())
    lst.append(tmp)
    largest = max(largest, tmp)

res = 0   # res가 답
low, high = 1, largest

while low <= high:
    mid = (low + high) // 2
    
    cnt = 0   # cnt는 잘라서 나온 랜선의 개수
    for i in range(K):
        cnt += lst[i] // mid
    
    if cnt >= N:
        res = mid
        low = mid + 1
    else:
        high = mid - 1

print(res)
    
