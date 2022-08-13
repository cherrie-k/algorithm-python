'''
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 
그 합이 최대인 자연수를 출력하세요. 
각 자연수의 자릿수의 합을 구하는 함수는 def digit_sum(x)를
꼭 작성해서 프로그래밍 하세요.

When N natural numbers are entered, 
find the sum of the digits of each natural number and 
print the maximum number of the sum of natural numbers.
Make sure to write def digit_sum(x) as the function 
that calculates the sum of the digits of each natural number.
'''
import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())
lst = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while x >= 1:
        sum += x % 10
        x = int(x / 10)
    return(sum)

max = 0

for i in range(N):
    val = digit_sum(lst[i])
    if val > max:
        max = val
        idx = i
    
print(lst[idx])
    
    
'''
다른 풀이 1 - int로만 처리
import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum
max = -2147000000 
for x in a:
    total = digit_sum(x)
    if total > max:
        max = total
        res = x
print(res)
'''

'''
다른 풀이 2 - int를 string으로 바꿔서 처리
import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
def digit_sum(x):
    sum = 0
    for i in str(x):    #정수를 string처리 해줌
        sum += int(i)   # 다시 정수로 바꿔줌
    return sum
max = -2147000000 
for x in a:
    total = digit_sum(x)
    if total > max:
        max = total
        res = x
print(res)
'''
    