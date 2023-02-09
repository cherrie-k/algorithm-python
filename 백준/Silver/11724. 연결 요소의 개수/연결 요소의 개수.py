import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[] for _ in range(n+1)]
visited = [False]*(n+1)

def dfs(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:  # 아직 방문 안한애들 방문
            dfs(i)

for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)  # 양방향으로 에지 더해주기
    
cnt = 0
 
for i in range(1, n+1):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)    
