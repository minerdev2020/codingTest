#include <string>
#include <vector>

using namespace std;

void dfs(string begin, string target, vector<string> words, int *answer, vector<bool> check, int ans){
    if(target == begin){
        if(*answer == 0)
           *answer = ans;
        else{
            if(*answer > ans)
                *answer = ans;
        }
        return;
    }
    for(int i = 0; i < words.size(); i++){
        if(check[i] == true)
            continue;
        int ck = 0;
        for(int j = 0; j < begin.size(); j++){
            if(begin[j] != words[i][j])
                ck++;
        }
        if(ck == 1 && check[i] == false){
            check[i] = true;
            dfs(words[i], target, words, answer, check, ans + 1);
        }
    }
}

int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    vector<bool> check;
    for(int i = 0; i < words.size(); i++){
        check.push_back(false);
    }
    dfs(begin, target, words, &answer, check, 0);
    return answer;
}
