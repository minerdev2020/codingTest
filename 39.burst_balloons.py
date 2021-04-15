# 다른 사람의 답안 참고함
class Solution:
    def maxCoins(self, nums: list) -> int:
        nums.insert(0, 1)
        nums.append(1)
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
                
        for l in range(1, n + 1):
            for left in range(n - l):
                right = left + l
                for k in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right])
        
        return dp[0][n - 1]
    
s = Solution()
print(s.maxCoins([3, 1, 5, 8]))
print(s.maxCoins([1, 5]))