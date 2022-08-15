'''
OX 문제는 맞거나 틀린 두 경우의 답을 가지는 문제를 말한다. 
여러 개의 OX 문제로 만들어진 시험에서 연속적으로 답을 맞히는 경우에는 
가산점을 주기 위해서 다음과 같이 점수 계산을 하기로 하였다. 
1번 문제가 맞는 경우에는 1점으로 계산한다. 
앞의 문제에 대해서는 답을 틀리다가 답이 맞는 처음 문제는 1점으로 계산한다. 
또한, 연속으로 문제의 답이 맞는 경우에서 두 번째 문제는 2점, 
세 번째 문제는 3점, ..., K번째 문제는 K점으로 계산한다. 틀린 문제는 0점으로 계산한다.
예를 들어, 아래와 같이 10 개의 OX 문제에서 답이 맞은 문제의 경우에는 
1로 표시하고, 틀린 경우에는 0으로 표시하였을 때, 
점수 계산은 아래 표와 같이 계산되어, 총 점수는 1+1+2+3+1+2=10 점이다.
          O X O O O X X O O X  
    채점| 1 0 1 1 1 0 0 1 1 0
    점수| 1 0 1 2 3 0 0 1 2 0
N개의 시험문제의 채점 결과가 주어졌을 때, 총 점수를 계산하시오.

The OX problem refers as a problem that has the answer of only two cases, right or wrong.
In order to give bonus points when the answer is correct in succession, 
the score is calculated as described below.
If Q#1 is correct, it's 1 point. When you get a question correct after it's been incorrect,
that first question with the correct answer is calculated as 1 point.
If the answer to the question is correct consecutively, 
the 2nd question is calculated as 2 points, the 3rd question is calculated as 3 points, 
and the K-th question is calculated as K points. 
The wrong questions are counted as zero points.
For example, if the result for 10 # of OX questions is as shown below, 
(1 for correct and 0 for incorrect) the score calculation will be executed as 
shown in the table below, and the total score is 1+1+2+3+1+2=10.
        O X O O O X X O O X
Grade | 1 0 1 1 1 0 0 1 1 0
Score | 1 0 1 2 3 0 0 1 2 0
Given the scoring results of N # of test questions, calculate the total score.
'''

import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())
lst = list(map(int, input().split()))

score = 0
cont = True
bonus = 0

for i in range(N):
    if lst[i] == 1:
        bonus += 1
        score += bonus
    elif lst[i] == 0:
        bonus = 0 
        score += bonus

print(score)
        