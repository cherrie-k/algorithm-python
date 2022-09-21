#import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())


def Factorial(num):
    res = 1 
    while (num >= 1):
        res = res  * num
        num = num - 1
        Factorial(num)
    return res
    
    
if n == 0:
    print(1)
else:
    print(Factorial(n))