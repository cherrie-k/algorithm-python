'''
채리의 농장은 N*N 격자판으로 이루어져 있으며, 
각 격자안에는 한 그루의 사과나무가 심어저있다. N은 항상 홀수이다. 
가을이 되어 사과를 수확해야 하는데 채리는 격자판안의 사과를 
수확할 때 다이아몬드 모양의 격자판만 수확하고 나머지 
격자안의 사과는 새들을 위해서 남겨놓는다.
만약 N이 5이면 아래 그림과 같이 진한 부분의 사과를 수확한다.
(그림 생략..^^)
채리가 수확하는 사과의 총 개수를 출력하세요.

Cherrie's farm is a form of N*N grid, 
and an apple tree is planted in each grid. The size of N is always odd. 
In autumn when Cherrie harvests apples, she only picks the apples in the
diamond-shaped are of the grid. She leaves the rest of the area for birds.
If N is 5, harvest the thick apple as shown in the figure below.
(skipped figure)
Print out the total number of harvested apples.
'''

import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())
lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))

res = 0

for a in range(N//2 + 1):
    for d in range(N//2 - a):
        del lst[a][0]
    for s in range(a * 2 + 1):
        res += lst[a][s]
    
for b in range(N - 1, N//2, -1):
    for d in range(b - N//2):
        del lst[b][0]
    for s in range((N - b) * 2 - 1):
        res += lst[b][s]

print(res)