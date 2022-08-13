'''
N명의 학생의 수학점수가 주어집니다. 
N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하세요.
평균과 가장 가까운 점수가 여러 개일 경우 
먼저 점수가 높은 학생의 번호를 답으로 하고, 
높은 점수를 가진 학생이 여러 명일 경우 
그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.

Math scores of N number of students will be given.
Find the average of N students (rounded to the first decimal place) 
and print out which student is the closest to the average among N students.
If there are multiple scores closest to the average, 
the number(index+1) of student with higher score is the answer, 
and if there are multiple students with high scores, 
the number(index+1) of students with the lowest student number(index+1) is the answer.
'''

import sys
#sys.stdin = open("input.txt", "rt")
    
N = int(input())
l = list(map(int, input().split()))

score = 0
for i in range(N):
    score += l[i]

score = round(score/N)

min = l[0]

for j in range(N):
    if abs(score - l[j]) < abs(score - min):
        min = l[j]

print(score, l.index(min)+1)

'''
다른 풀이
import sjys
sys.stdin = open("input.txt", "r")
n = int(input())
a = list(mp(int, input().split()))
ave = round(sum(a)/n)
min = 2147000000
for idx, x in enumerate(a):
    # idx에는 list a 에 있는 인덱스 값을, x에는 해당 인덱스에 있는 원소값을 대입해줌
    tmp = abs(x-ave)
    if tmp < min:
        min = tmp
        score = x 
        res = idx + 1
    elif tmp == min:    # 평균값과의 거리가 같을 때
        if x > score:
            score = x
            res = idx + 1 
print(ave, res)
'''