def solution(num):
    if num[0] == '0' or len(num) > 5000:
        return 0
    dp = [0 for _ in range(len(num))]
    dp[0] = 1
    for i in range(1, len(num)):
        if num[i] != '0':
            dp[i] = dp[i-1] % 1000000
        tmp = int(num[i-1]) * 10 + int(num[i])
        if tmp >= 10 and tmp <= 26:
            dp[i] = (dp[i-2] + dp[i]) % 1000000 if i != 1 else dp[i] + 1

    return dp[len(num) - 1] % 1000000

num = input()
n = solution(num)
print(n)
