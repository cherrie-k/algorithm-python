import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
k = int(input())
sensor = sorted(list(map(int, input().split())))

lst = []
for i in range(0, n-1):
    lst.append(sensor[i+1] - sensor[i])
    

lst.sort()

print(sum(lst[:n-k]))