import sys
#sys.stdin = open("input.txt", "rt")

num = list(input().strip())

dp = [0 for _ in range(len(num) + 1)]
dp[0], dp[1] = 1, 1


if num[0] == "0":     #암호 잘못된경우
    print(0)
else:
    for i in range(2, len(num) + 1):
        if int(num[i - 1]) > 0:
            dp[i] += dp[i - 1]
        convertInt = int(num[i - 2] + num[i - 1])
        if 10 <= convertInt <= 26:
            dp[i] += dp[i - 2]
            
    print(dp[len(num)] % 1000000)