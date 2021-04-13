# 내 풀이
def solution(A):
    if not A:
        return 0
    
    length = len(A)
    count_map = [[0, 0] * (2 ** i) for i in range(length)]
    count_map[0][0] = A[0]
    count_map[0][1] = -A[0]
    for i in range(1, length):
        k = 0
        for j in range(2 ** i):
            count_map[i][k] = count_map[i - 1][j] + A[i]
            count_map[i][k + 1] = count_map[i - 1][j] - A[i]
            k += 2

    return min(list(map(abs, count_map[length - 1])))

# 다른 사람의 풀이 1
def solution1(A):
    if not A:
        return 0
    
    A = list(map(abs, A))
    all_sum = sum(A)
    count_map = {}
    for a in A:
        if a not in count_map:
            count_map[a] = 0
            
        count_map[a] += 1
    
    length = all_sum // 2 + 1
    dp = [-1 for _ in range(length)]
    dp[0] = 0

    for key in count_map:
        for i in range(length):
            if dp[i] >= 0:
                dp[i] = count_map[key]
                
            elif i >= key and dp[i - key] > 0:
                dp[i] = dp[i - key] - 1
                
    result = all_sum
    for i in range(length):
        if dp[i] >= 0:
            result = min(result, all_sum - i * 2)
            
    return result

# 다른 사람의 풀이 2
def solution2(A):
    N = len(A)
    A = list(map(abs, A))   
    S = sum(A)
    dp = [0 for _ in range(S + 1)]
    dp[0] = 1
    for j in range(N):
        for i in range(S, -1, -1):
            if (dp[i] == 1) and (i + A[j] <= S):
                dp[i + A[j]] = 1
                
    result = S
    for i in range(S // 2 + 1):
        if dp[i] == 1:
            result = min(result, S - 2 * i)
            
    return result

print(solution([]))             # 0
print(solution([1]))            # 1
print(solution([1, 2, 1, 3]))   # 1
print(solution([1, 5, 2, -2]))  # 0
print(solution([0, 0, 0, 0]))   # 0
print(solution([1, -1, -2, 4])) # 0
print(solution([1, 8, 1, 8]))   # 0
print(solution([5, 20, 5, 10, 5, 20, 0, 8])) # 3