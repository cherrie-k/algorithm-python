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
