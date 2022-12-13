import sys
#sys.stdin = open("input.txt", "rt")

S = set()
input = sys.stdin.readline
M = int(input())

for i in range(M):
    cmd = input().split()
    if cmd[0] == "all":
        S = set([i for i in range(1, 21)])
    elif cmd[0] == "empty":
        S = set()
    elif cmd[0] == "add":
        S.add(int(cmd[1]))
    elif cmd[0] == "check":
        print (1 if int(cmd[1]) in S else 0)
    elif cmd[0] == "remove":
        S.discard(int(cmd[1]))
    elif cmd[0] == "toggle":
        if int(cmd[1]) in S:
            S.discard(int(cmd[1]))
        else:
            S.add(int(cmd[1]))
        
