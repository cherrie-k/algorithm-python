'''
N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 
같은 경우(회문 문자열)이면 YES를 출력하고 아니면 NO를 출력하세요.
단 회문을 검사할 때 대소문자를 구분하지 않습니다.

You will receive N number of string data.
If it's the same whether it's read from the begging or end 
(being a palindromeS), print YES. If not (a palindrome), print NO. 
Consider the string as case-insensitive.
'''

import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())

for n in range(N):
    print("#", n + 1, sep='', end=' ')
    lst1 = list(input().lower())
    a = ''.join(map(str, lst1))
    lst1.reverse()
    b = ''.join(map(str, lst1))
    
    if a == b:
        print("YES")
    else: 
        print("NO")
    
    
'''
각 단어 input을 리스트로 받은 후, 그 리스트를 string으로 전환해서 저장.
그 후 리스트.reverse()해서 다른 string으로 저장.
두 string을 비교해서 회문인지 아닌지 판별.
리스트랑 리스트.reverse()를 바로 비교하지 않은 이유:
리스트는 deep copy가 안돼서 주소값을 공유하기 떄문에
list1 = list2를 하고 list2.reverse()를 해버리면, 
list1도 reverse 돼버려서 회문 판단 불가해짐.  
'''


'''
다른 풀이

import sys
#sys.stdin=open("input.txt", "r")
n=int(input())
for i in range(1, n+1):
    str=input()
    str=str.upper()
    #반반씩 나눠서 같은지 비교
    for j in range(len(str)//2):
        #앞에 반이랑 뒤에 반 같은지 비교
        #뒤에부터 인덱스 넣는거는 -값으로 접근
        if str[j]!=str[-1-j]:
            print("#%d NO" %i)
            break
    else:
        print("#%d YES" %i)




<다른코드>

import sys
sys.stdin=open("input.txt", "r")
n=int(input())
for i in range(n):
    str=input()
    str=str.upper()
    if str==str[::-1]:
        # ::-1로 string reverse 시켜줌
        print("#%d YES" %i)
    else:
        print("#%d NO" %i)
'''