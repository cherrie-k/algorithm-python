import sys
input = sys.stdin.readline  # 입력빠르게
#sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
lst = list(map(int, input().split()))
res = [0]
tmp = 0

for x in lst:
    tmp = tmp + x
    res.append(tmp)
    
for i in range(m):
    i, j = map(int, input().split())
    print(res[j] - res[i-1])

