#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> triangle) {
    int answer = 0;
    vector<int> ans_list;
    ans_list.push_back(triangle[0][0]);
    
    for(int i = 1; i < triangle.size(); i++){
        vector<int> new_anslist;
        for(int j = 0; j <= i; j++){
            int check1 = 0, check2 = 0;
            if(j != i){
                check1 = triangle[i][j] + ans_list[j];
                
            }
            if(j != 0){
                check2 = triangle[i][j] + ans_list[j-1];
            }
            if(check1 >= check2)
                new_anslist.push_back(check1);
            else
                new_anslist.push_back(check2);
        }
        ans_list = new_anslist;
    }
    for(int i = 0; i < ans_list.size(); i++){
        if(ans_list[i] > answer)
            answer = ans_list[i];
    }
    return answer;
}
