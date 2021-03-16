def solution(num):
    dp = [0 for _ in range(num*3 + 1)]
    dp[num] = 1
    for i in reversed(range(1, num)):
        if dp[i*3]:
            dp[i] = dp[i*3] + 1
        if(dp[i*2]):
            dp[i] = min(dp[i*2] + 1, dp[i]) if dp[i] else dp[i * 2] + 1
        dp[i] = min(dp[i+1] + 1, dp[i]) if dp[i] else dp[i + 1] + 1
    return dp[1] - 1


num = int(input())
print(solution(num))
