#include <string>
#include <vector>

using namespace std;

void dfs(int *answer, vector<int> numbers, int target, int now_num){
    if(numbers.size() == 0){
        if(now_num == target)
            (*answer)++;
        return;
    }
    int a = numbers.back();
    numbers.pop_back();
    dfs(answer, numbers, target, now_num + a);
    dfs(answer, numbers, target, now_num - a);
}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    dfs(&answer, numbers, target, 0);
    return answer;
}
