def solution(total):
    dp = [0 for _ in range(total + 1)]
    for i in range(2, total + 1):
        temp = []
        if not i % 3:
            temp.append(1 if i // 3 == 1 else 1 + dp[i // 3])
            
        if not i % 2:
            temp.append(1 if i // 2 == 1 else 1 + dp[i // 2])
        
        temp.append(1 + dp[i - 1])
        dp[i] = min(temp)
          
    return dp[total]

print(solution(2))  # 1
print(solution(10)) # 3
print(solution(11)) # 4
print(solution(1))  # 0