'''
N개의 자연수가 입력되면 각 자연수를 뒤집은 후 
그 뒤집은 수가 소수이면 그 수를 출력하세요. 
예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력한다. 
단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시한다. 
뒤집는 함수인 def reverse(x) 와 
소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성한다.

When N number of positive integers are entered, 
flip each integers and print the flipped number 
if the flipped number is a prime number. 
For example, if you flip 32, 23 is a prime number. Print 23.
If you flip 910, you have to digitize it as 19. 
Ignore consecutive zeros from the first digit. 
Use def reverse(x) as a function of flipping, 
and def isPrime(x), as a function of determining if it is a prime number.
'''

import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
lst = list(map(int, input().split()))

def reverse(x):
    return x

def isPrime(x):
    return True

print(lst)