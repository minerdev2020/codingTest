def solution(total):
    dp = [0 for _ in range(total + 1)]
    for i in range(1, total + 1):
        min_sugar = 9999
        for j in range(1, i + 1):
            if (not j % 3 or not j % 5) and dp[i - j] != -1:
                sugar =  j // 5 if not j % 5 else j // 3
                min_sugar = min(min_sugar, sugar + dp[i - j])
        
        if min_sugar != 9999:
            dp[i] = min_sugar
            
        else:
            dp[i] = -1
        
    return dp[total]

print(solution(18)) # 4
print(solution(4))  # -1
print(solution(6))  # 2
print(solution(9))  # 3
print(solution(11)) # 3
