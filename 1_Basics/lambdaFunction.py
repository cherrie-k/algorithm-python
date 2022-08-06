'''
Lambda Function
(a.k.a 익명의 함수, 람다 표현식)
'''

# 그냥 함수
def plus_one(x):
    return x + 1
print(plus_one(2))

# 람다 함수
plus_two = lambda x : x + 2
print(plus_two(2))


''' 람다 함수는 내장 함수의 인자로 사용하기 좋음 '''

a = [1, 2, 3]
print(list(map(plus_one, a)))
# map은 리스트의 요소를 지정된 함수로 처리해주는 함수
print(list(map(lambda x : x + 2, a)))
# map이라는 함수에 인자로 lambda함수를 가져다 씀