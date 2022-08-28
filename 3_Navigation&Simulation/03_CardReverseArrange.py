'''
1부터 20까지 숫자가 하나씩 쓰인 20장의 카드가 오름차순으로 한 줄로 놓여있다. 
각 카드의 위치는 카드 위에 적힌 숫자와 같이 1부터 20까지로 나타낸다.
이제 여러분은 다음과 같은 규칙으로 카드의 위치를 바꾼다: 
구간 [a, b] (단, 1 ≤ a ≤ b ≤ 20)가 주어지면 
위치 a부터 위치 b까지의 카드를 현재의 역순으로 놓는다.
예를 들어, 현재 카드가 놓인 순서가 1~20(오름차순)이고 구간이 [5, 10]으로 주어진다면, 
위치5부터 위치 10까지의 카드 5, 6, 7, 8, 9, 10을 역순으로 하여 10, 9, 8, 7, 6, 5로 놓는다.
이제 전체 카드가 놓인 순서는 1, 2, 3, 4, 10, 9, 8, 7, 6, 5, 11, 12, 13 ~ 20 이다.
이 상태에서 구간 [9, 13]이 다시 주어진다면, 위치 9부터 위치 13까지의 카드 
6, 5, 11, 12, 13을 역순으로 하여 13, 12, 11, 5, 6으로 놓는다. 
이제 전체 카드가 놓인 순서는 1, 2, 3, 4, 10, 9, 8, 7, 13, 12, 11, 5, 6, 14, 15 ~ 20 이다.
오름차순으로 한 줄로 놓여있는 20장의 카드에 대해 10개의 구간이 주어지면, 
주어진 구간의 순서대로 위의 규칙에 따라 순서를 뒤집는 작업을 연속해서 처리한 뒤 
마지막 카드들의 배치를 구하는 프로그램을 작성하시오.

Twenty cards with numbers written one by one from 1 to 20 are placed linearly in ascending order.
The location of each card is indicated by a number from 1 to 20, 
which is the same as the number written on the card.
Now, reposition the card with the following rules:
When given the section [a, b] (1 ≤ a ≤ b ≤ 20),
arrange the cards from position a to position b in reverse order.
For example, if the current card is placed in order of 1 to 20 (in ascending order) 
and the section is given as [5, 10], place the cards 5, 6, 7, 8, 9, 10 in reverse order 
from position 5 to position 10, in the order as 10, 9, 8, 7, 6, 5.
Now, the arrange of the entire card is 1, 2, 3, 4, 10, 9, 8, 7, 6, 5, 11, 12, 13 ~ 20.
If the section [9, 13] is given again in this state, place the cards
6, 5, 11, 12, 13 from position 9 to position 13 in reverse order to 13, 12, 11, 5, 6.
The arrange of the entire card is now 1, 2, 3, 4, 10, 9, 8, 7, 13, 12, 11, 5, 6, 14, 15 ~ 20.
You will be given 10 sections for 20 cards(which are in ascending order),
so write a program to find the placement of the final cards after successively 
processing the reverse sequence according to the rules above.
'''

import sys
#sys.stdin = open("input.txt", "rt")

lst = [i for i in range(1, 21)]

for t in range(10):
    tmp = []
    a, b = map(int, input().split())
    for i in range(b-1, a-2, -1):
        x = lst.pop(i)
        tmp.append(x)
    
    for j in range(b - a + 1):
        y = tmp.pop()
        lst.insert(a-1, y)


for n in lst:
    print(n, end=' ')
    
'''
다른 풀이

import sys
sys.stdin = open("input.txt", "rt")
a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    # 절반 나눠서 서로 swap 해주기
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]        
a.pop(0)    # 제일 앞에 있는 0 빼줌
for x in a:
    print(x, end=' ')
'''