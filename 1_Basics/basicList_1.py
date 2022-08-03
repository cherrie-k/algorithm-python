'''Basic List Functions'''

import random as r

'''
Empty Lists
a = []
b = list()
print(a)
print(b)
'''

a = [1, 2, 3, 4, 5]
print(a)
a.append(7)     # list 끝에 추가
print(a)
a.insert(3, 10) # list의 3번 인덱스에 10 끼워넣기
print(a)
a.pop()         # 맨 뒤 값 제거
print(a)
a.pop(3)        # 3번 인덱스에 있는 값 제거
print(a)
a.remove(2)     # 4라는 값을 찾아서 제거
print(a)
print(a.index(4))  # 3이라는 값이 위치한 인덱스 출력

b = list(range(1, 11))
print(b)
print(sum(b))
print(max(b))   # b라는 리스트에서 가장 큰 값 찾기
print(b.index(max(b)))  #b라는 리스트에서 가장 큰 값의 인덱스 출력
print(min(b))   # b라는 리스트에서 가장 작은 값 찾기
print(min(3, 5, 6, 2, 1, 9))    # 주어진 리스트에서 min값 찾기

print(b)
r.shuffle(b)    # import random as r 위에서 해줘야함
print(b)
b.sort()                # 오름차순으로 정렬
print(b)
b.sort(reverse=True)    # 내림차순으로 정렬
print(b)
b.clear()       # 리스트 비워줌
print(b)        # empty list 출력

