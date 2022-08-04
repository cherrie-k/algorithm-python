'''Basic List Functions (2)'''


a = [23, 12, 36, 53, 19]
print(a[:3])    # 리스트에서 3번 인덱스까지 출력

'''리스트 출력'''
for i in range(len(a)):
    print(a[i], end = " ")

print() #아래 위 완전히 동일

for j in a:
    print(j, end = ' ')

print()
# index 번호의 값에 접근
for x in enumerate(a):
    print(x) 
# enumerate를 사용하면 인덱스 번호와, 거기 있는 값을 tuple로 리턴해줌
# tuple은 list와 달리 원소 변경 불가
for x in enumerate(a):
    print(x[0], x[1])
    # tuple의 원소에 접근

print() # 아래 위 동일

for index, value in enumerate(a):
    print(index, value)

print()

if all(50 > x for x in a):
    # a 안의 모든 원소가 60보다 작을 때, all은 true를 리턴
    print("Yeah")
else: print("Nah")
    
print()   
    
if any(50 > x for x in a): 
    # 하나라도 조건문이 참이 되면 any는 true를 리턴
    print("Yeah")
else: 
    print("Nah")