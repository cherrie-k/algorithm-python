'''
자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하세요.
만약 20이 입력되면 1부터 20까지의 소수는 
2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
제한시간은 1초입니다.

When a positive integer N is entered, 
print out the number of prime numbers from 1 to N. 
If 20 is entered, 2, 3, 5, 7, 11, 13, 17, and 19 will be printed.
The time limit is 1 second.
'''



'''
에라토스테네스 체를 활용해서 풀이
"소수의 배수는 소수가 될 수 없다 -> 걸러낸다"

Used the "Sieve of Eratosthenes" to satisfy the time limit
'''

import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
check = [0]*(n+1)
# 리스트 check의 인덱스 값: 1~n까지 확인해야 할 값
# 리스트 내 원소가 0 -> 체크 안된 것. 소수인것
# 리스트 내 원소가 1 -> 체크 된 것. 소수가 아닌것
count = 0

for i in range(2, n+1): 
# 1은 소수 제외, n+1까지 range 설정해줘야 n까지 돌음
    if check[i] == 0:   # 체크 안된것 -> 소수
        count += 1  # 소수의 수 ++
        for j in range(i, n+1, i):  
        # i부터 n+1까지 i step씩 반복문 돌면서 i의 배수들을 체크해줌 -> 소수 아니라고 표시해줌
            check[j] = 1   # ch[j]의 원소는 소수가 아니라고 표시
print(count)



    
'''
내가 했던, 시간 제한 충족 못하는 풀이
import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())

lst = set()

def isPrime(x):
    count = x - 1
    for i in range(2, x+1):
        for j in range (2, i):
            if i % j == 0:
                count -= 1
                break
    return count
            

print(isPrime(N))
'''