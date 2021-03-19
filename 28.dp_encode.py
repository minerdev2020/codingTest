def solution(msg):
    if len(msg) > 5000:
        return 0
    
    elif msg[0] == '0':
        return 0
    
    elif len(msg) == 1:
        return 1
    
    dp = [0 for _ in range(len(msg) + 1)]
    dp[1] = 1
    
    if 0 < int(msg[0:2]) <= 26:
        dp[2] = 1 if not int(msg[0:2]) % 10 else 2
        
    else:
        dp[2] = 0 if not int(msg[0:2]) % 10 else 1

    for i in range(3, len(msg) + 1):        
        if msg[i - 2] != '0' and 0 < int(msg[i-2:i]) <= 26:
            dp[i] += dp[i - 2]
        
        if msg[i - 1] != '0':
            dp[i] += dp[i - 1]
        
    return dp[len(msg)] % 1000000
    
print(solution('25114')) # 6
print(solution('52114')) # 5
print(solution('205'))   # 1
print(solution('250'))   # 0
print(solution('502'))   # 0