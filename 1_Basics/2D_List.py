'''
Creating and accessing 2-Dimensional Lists
'''

a = [[0]*3 for _ in range(4)]
print(a)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
a[0][1] = 1
print(a)
# [[0, 1, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
a[1][1] = 2
print(a)
#[[0, 1, 0], [0, 2, 0], [0, 0, 0], [0, 0, 0]]

#표처럼 출력
for x in a:
    print(x)
    
for x in a:
    #일차원 리스트의 원소 값 하나하나에 접근
    for y in x:
        print(y, end = ' ')
    print()