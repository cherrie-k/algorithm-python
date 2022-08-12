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
돌아가기는 하는데 시간 제한이 해결 안됨,,, 
다시 고쳐볼것
'''

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
    
