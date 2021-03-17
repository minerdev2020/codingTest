def solution(total):
    if total == 1:
        return 1
    
    elif total == 2:
        return 2
    
    elif total == 3:
        return 4
    
    dp = [0 for _ in range(total + 1)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, total + 1):
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

    return dp[total]

T = int(input())
numbers = []
for _ in range(T):
    numbers.append(int(input()))
    
for n in numbers:
    print(solution(n))  # 7, 44, 274
    
print(solution(4))  # 7
print(solution(7))  # 44
print(solution(10)) # 274
print(solution(1))  # 1
print(solution(2))  # 2
print(solution(3))  # 4