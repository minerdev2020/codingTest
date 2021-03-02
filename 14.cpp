#include <algorithm>
#include <vector>

using namespace std;

int solution(int N, int number) {
    int answer = 0;
    
    vector<int> dp[8+1];
    int base = 0;
    for(int i = 1; i < 9; i++){
        base = base * 10 + N;
        dp[i].push_back(base);
    }

    for(int i = 1; i < 9; i++){
        for(int j = 1; j < i; j++){
                 for(auto& x:dp[j]){
                    for(auto& y:dp[i-j]){
                        dp[i].push_back(x + y);
                        dp[i].push_back(x - y);
                        dp[i].push_back(x * y);
                        if(y != 0)    
                            dp[i].push_back(x / y);
                    }
                 }
        }
        if(count(dp[i].begin(),dp[i].end(),number) > 0){
            answer = i;
            break;
        }
    }
    
    return answer==0?-1:answer;
}
