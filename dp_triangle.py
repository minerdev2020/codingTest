# 내 풀이
answer_tri = []

def dp(step, now, triangle):
    if answer_tri[step][now] != -1:
        return answer_tri[step][now]

    if step + 1 == len(triangle):
        answer_tri[step][now] = triangle[step][now]
        return triangle[step][now]
    
    max_num = -1
    for child in range(now, now + 2):
        temp = dp(step + 1, child, triangle)
            
        if max_num < temp:
            max_num = temp
    
    answer_tri[step][now] = triangle[step][now] + max_num
    return triangle[step][now] + max_num

def solution(triangle):
    for i in range(len(triangle)):
        answer_tri.append([-1 for j in range(i + 1)])

    return dp(0, 0, triangle) 

# 다른 사람의 풀이 1
def solution1(triangle):
    dp = []
    for t in range(1, len(triangle)):
        for i in range(t+1):
            if i == 0:
                triangle[t][0] += triangle[t-1][0]
            elif i == t:
                triangle[t][-1] += triangle[t-1][-1]
            else:
                triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
                
    return max(triangle[-1])

# 다른 사람의 풀이 2
def solution(triangle):
    memo = {}
    answer = f(triangle, 0, 0, memo)
    return answer

def f(triangle, i, j, memo):
    if i == len(triangle)-1:
        return triangle[i][j]

    if (i,j) in memo:
        return memo[(i,j)]

    a = f(triangle, i+1, j, memo)
    b = f(triangle, i+1, j+1, memo)
    x = triangle[i][j] + max(a, b)

    memo[(i,j)] = x

    return x

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
print(answer_tri)