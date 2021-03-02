# 내 풀이 (시간 초과)
from copy import deepcopy

all_routes = {}
target = None

def insert(routes, now):
    for route in routes:
        route.append(now)

def dp(now, puddles):
    if now in puddles:
        return [[]]

    elif now == target:
        return [[now]]
    
    elif now in all_routes:
        if all_routes[now]:
            return deepcopy(all_routes[now])
        
        else:
            return [[]]
    
    all_routes[now] = []
    temp1 = [[]]
    temp2 = [[]]
    if now[0] != target[0]:
        temp1 = dp((now[0] + 1, now[1]), puddles)
 
    if now[1] != target[1]:
        temp2 = dp((now[0], now[1] + 1), puddles)

    if not temp2[0] and not temp1[0]:
        return [[]]
    
    elif temp1[0] and not temp2[0]:
        insert(temp1, now)
        all_routes[now]= temp1
        
    elif temp2[0] and not temp1[0]:
        insert(temp2, now)
        all_routes[now] = temp2
 
    elif len(temp1[0]) < len(temp2[0]):
        insert(temp1, now)
        all_routes[now]= temp1   
    
    elif len(temp1[0]) > len(temp2[0]):
        insert(temp2, now)
        all_routes[now]= temp2   
        
    else:
        insert(temp1, now)
        insert(temp2, now)
        all_routes[now] = temp1
        all_routes[now] += temp2

    return deepcopy(all_routes[now])

def solution(m, n, puddles):
    global target
    target = (m, n)
    
    puddles = list(map(tuple, puddles))
    answer = dp((1, 1), puddles)
    
    if not answer[0]:
        return 0
    
    return len(answer) % 1000000007

# 다른 사람의 풀이
def solution1(m, n, puddles):
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    print(dp)
    for p in puddles:
        dp[p[0]][p[1]] = -1
        
    dp[1][1] = 1
    for x in range(1, m + 1):
        for y in range(1, n + 1):
            if dp[x][y] == -1:
                dp[x][y] = 0
                
            else:
                if x == 1 and y == 1:
                    continue

                else:
                    dp[x][y] = (dp[x - 1][y] + dp[x][y - 1]) % 1000000007
          
    print(dp)
    return dp[m][n]

print(solution(4, 3, [[2, 2]]))
for key, values in all_routes.items():
    print(key)
    for value in values:
        print(value)

print(solution1(4, 3, [[2, 2]]))