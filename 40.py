class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp=[[0] *col for j in range(row)]
        for i in range(col):
            if obstacleGrid[0][i]==1:
                break
            dp[0][i]=1
        for j in range(row):
            if obstacleGrid[j][0]==1:
                break
            dp[j][0]=1
        for i in range(1,row):
            for j in range(1,col):
                if obstacleGrid[i][j] != 1:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[row-1][col-1]
        
