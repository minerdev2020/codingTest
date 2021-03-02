#include <string>
#include <vector>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    long long dp[101][101] = { 0, };
    int map[101][101] = { 0, };
    for(int i = 0; i < puddles.size(); i++){
        map[puddles[i][1]-1][puddles[i][0]-1] = 1;
    }
    dp[0][0] = 1;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(map[i][j]) 
                continue;
            int next_x = j + 1;
            int next_y = i + 1;//아래쪽 이동.
            if(next_x < m) 
                dp[i][next_x] = (dp[i][next_x] + dp[i][j]) % 1000000007;
            if(next_y < n) 
                dp[next_y][j] = (dp[next_y][j] + dp[i][j]) % 1000000007;
        }
    }
    return dp[n-1][m-1];
}
