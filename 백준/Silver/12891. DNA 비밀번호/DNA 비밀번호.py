s, p = map(int, input().split())
lst = list(input())
minList = list(map(int, input().split()))
dic = {'A': minList[0], 'C': minList[1], 'G':minList[2], 'T':minList[3]}
cnt = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

res = 0

for i in range(s - p + 1):
    flag = True
    if i == 0:
        for j in range(p):
            cnt[lst[j]] += 1
    else:
        cnt[lst[i+p-1]] += 1
        cnt[lst[i-1]] -= 1
        
    for i in ('A', 'C', 'G', 'T'):
        if cnt[i] < dic[i]:
            flag = False
            break
    
    if flag:
        res += 1
        
print(res)