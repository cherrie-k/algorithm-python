'''
Creating Functions
특정 작업을 하는 반복적으로 나타나는 코드를 함수로 빼둠
'''


#CPP과 달리 복수의 값 리턴 가능 !
from re import L


def add(a, b):
    c = a + b
    d = a - b
    return c, d
x = add(3, 5)
print(x)
# (8, -2) 출력 

# 소수인지 아닌지 판단하는 함수
def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


y = [12, 13, 7, 9, 19]
for i in y:
    if isPrime(i):
        print(i, end=' ')