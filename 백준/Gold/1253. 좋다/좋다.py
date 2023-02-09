import sys
input = sys.stdin.readline  # 입력빠르게

n = int(input())
lst = list(map(int, input().split()))

lst.sort()

res = 0
for i in range(n):
    target = lst[i]
    s = 0
    e = n - 1
    while s < e:
        if lst[s] + lst[e] == target:
            if s != i and e != i:
                res += 1        
                break
            elif s == i:
                s += 1
            elif e == i:
                e -= 1
        elif(lst[s] + lst[e] < target):
            s += 1
        else:
            e -= 1

print(res)
            