# 다른 사람의 풀이
def solution(money):
    house_size = len(money)
    dp = [[0, 0] for i in range(house_size)]
    
    # 첫번째 집을 털었을때
    dp[0][0] = money[0]
    dp[1][0] = money[0]
    
    # 첫번째 집을 안 털었을때
    dp[1][1] = money[1]
    
    for i in range(2, house_size):
        if i < house_size - 1:
            dp[i][0] = max(dp[i - 2][0] + money[i], dp[i - 1][0])
        
        dp[i][1] = max(dp[i - 2][1] + money[i], dp[i - 1][1])
    
    print(dp)
    return max(dp[-2][0], dp[-1][1])

print(solution([1, 2, 3]))