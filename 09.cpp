#include <string>
#include <vector>

using namespace std;

void bfs(bool *temp, vector<vector<int>> computers, int num, int n){
    if(temp[num] == true)
        return;
    temp[num] = true;
    for(int i = 0;i < n; i++){
        if(computers[num][i] == 1){
            bfs(temp, computers, i, n);
        }
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    bool *temp = new bool[n];
    for(int i = 0; i < n; i++)
        temp[i] = false;
    for(int i = 0; i < n; i++){
        if(temp[i] == true)
            continue;
        bfs(temp, computers, i, n);
        answer++;
    }
    return answer;
}
