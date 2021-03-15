#dp
def solution(num):
    dp = [0 for _ in range(20000)]
    dp[3] = dp[5] = 1
    for i in range(6, num + 1):
        if dp[i-3]:
            dp[i] = dp[i-3] + 1
        if(dp[i-5]):
            if(dp[i]):
                dp[i] =  min(dp[i]+1 , dp[i - 5] + 1)
            else:
                dp[i] = dp[i-5] + 1
    if dp[num] == 0:
        return -1
    else:
        return dp[num]


num = int(input())
print(solution(num))

#greedy
N = int(input()) 
three = 0
five = N // 5

rest = N % 5

if rest != 0:
    for i in range(five, -1, -1):
        if rest % 3 == 0:
            three = rest // 3
            break
        five -= 1
        rest += 5

result = five + three

if result < 1:
    result = -1
print(result)
