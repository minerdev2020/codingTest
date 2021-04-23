class Solution:
    # 내 풀이 (시간 초과)
    def divide(self, dividend: int, divisor: int) -> int:
        if not dividend:
            return 0
                    
        dividend_temp = abs(dividend)
        divisor_temp = abs(divisor)
        
        print(dividend_temp)
        print(divisor_temp)
        
        answer = 0
        while True:
            dividend_temp -= divisor_temp
            if dividend_temp < 0:
                break
            
            answer += 1
            
        if dividend < 0 and divisor < 0 or dividend > 0 and divisor > 0:
            return min(2 ** 31 - 1, answer)
        
        else:
            return max(-2 ** 31, -answer)
            
    # 다른 사람의 풀이
    def divide1(self, dividend: int, divisor: int) -> int:
        x = dividend
        y = divisor
        ans = 0
        xx, yy = abs(x), abs(y)
        for i in range(32, -1, -1):
            if xx >= (yy << i):
                xx -= (yy << i)
                ans += (1 << i)
        
        if (x > 0 and y < 0) or (x < 0 and y > 0): 
            ans = -ans
        
        return min(2 ** 31 - 1, max(-2 ** 31, ans))
    
solution = Solution()
print(solution.divide(10, 3))   # 3
print(solution.divide(7, -3))   # -2
print(solution.divide(0, 1))    # 0
print(solution.divide(1, 1))    # 1
print(solution.divide(-1, 1))   # -1
print(solution.divide(-1, -1))  # 1
print(solution.divide(-2147483648, -1))  # 2147483647