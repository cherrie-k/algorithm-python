import sys
#sys.stdin = open("input.txt", "rt")

n  = int(input())
mod = 1000000007

def fac(v):
    ret = 1
    for i in range(1, v+1):
        ret = ret * i
    return ret

dp = [0] * 100010
dp[0] = 1
#dp[2] = 2

for i in range(2, n+1):
    dp[i] = (i-1)*((dp[i-1]+dp[i-2])%mod)%mod

print((dp[n]*fac(n))%mod)
