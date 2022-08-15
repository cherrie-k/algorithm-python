'''
N개의 숫자로 이루어진 숫자열이 주어지면 
해당 숫자열중에서 s번째부터 e번째 까지의 수를 오름차순 
정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램
Given a string that consists of N numbers,
print the k-th number between sth to eth,
which are among the number string in ascending order 
'''


import sys
#sys.stdin = open("input.txt", "rt")

T = int(input())    # number of cases
for t in range(T):
    n, s, e, k = map(int, input().split())  # 띄어쓰기 된걸 하나씩 읽어서 숫자에 mampping함
    l = list(map(int, input().split()))
    l = l[ s-1 : e]
    l.sort()
    print("#%d %d" %(t+1, l[k-1]))