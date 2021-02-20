#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    for(int i = 1; i <= yellow; i++){
        if(yellow % i != 0)
            continue;
        int j = yellow / i;
        if(i > j)
            break;
        int tp1 = (i + 2) * (j + 2);
        int tp2 = brown + yellow;
        if(tp1 == tp2){
            answer.push_back(j + 2);
            answer.push_back(i + 2);
            break;
        }
            
    }
    return answer;
}
