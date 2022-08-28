'''
문자와 숫자가 섞여있는 문자열이 주어지면 
그 중 숫자만 추출하여 그 순서대로 자연수를 만든다.
만들어진 자연수와 그 자연수의 약수 개수를 출력한다.
만약 “t0e0a1c2h0er”에서 숫자만 추출하면 0, 0, 1, 2, 0 이고
이것을 자연수를 만들면 120이 된다. 즉 첫 자리 0은 자연수화 할 때 무시한다. 
출력은 120를 출력하고, 다음 줄에 120의 약수의 개수를 출력하면 된다.
추출하여 만들어지는 자연수는 100,000,000을 넘지 않습니다.

Given a string of letters and numbers combined, extract only the numbers in it,
and create a positive integer in the extracted number. 
Print the positive integer and the number of divisors of the integer.
If the given string is "t0e0a1c2h0er," the numbers 0, 0, 1, 2, 0 will be extracted.
If you make a positive integer with it, it would be 120. Ignore the zeros in the beginning. 
The printed output would be 120 and the number of 120's divisors.
The integer produced by extraction does not exceed 100,000,000.
'''

'''
.isdigit() 함수 사용. 
'''

from curses.ascii import isdigit
import sys
#sys.stdin = open("input.txt", "rt")

lst = list(input())
a = ''
count = 0

for i in lst:
    if i.isdigit():
        a = a + i

a = int(a)   

for i in range(1, a + 1):
    if a % i == 0:
        count += 1

print(a, count, sep = "\n")


'''
다른 풀이

import sys
sys.stdin = open("input.txt", "rt")
s = input()
res = 0
for x in s:
    #s가 리스트가 아니더라도 하나씩 접근 가능
    if x.isdigit():
        #참고: .isdecimal은 0~9 까지의 숫자만 확인해줌. 이 문제에서는 사용 가능!
        res = res*10+int(x)
        
cnt = 0
for i in range(1, res+1):
    if res%i == 0:
        cnt += 1
print(cnt)
    
'''