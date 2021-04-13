class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = 1
        for y in range(m):
            for x in range(n):
                dp[y][x + 1] += dp[y][x]
                dp[y + 1][x] += dp[y][x]
                
        print(dp)
        return dp[m - 1][n - 1]
        
solution = Solution()
print(solution.uniquePaths(3, 7))