#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    vector<string>  temp;
    unordered_map<string, int> hash_map;
    for(int i = 0; i < clothes.size(); i++){
        if(hash_map[clothes[i][1]] == 0){
            temp.push_back(clothes[i][1]);
        }
        hash_map[clothes[i][1]]++;
    }
    for(int i = 0; i < temp.size(); i++){
        answer *= hash_map[temp[i]] + 1;
    }
    return answer - 1;
}

/*python
def solution(clothes):
    answer = 1
    hash_map = dict()
    for cloth in clothes:
        if cloth[1] not in hash_map.keys():
            hash_map[cloth[1]] = 1
        else:
            hash_map[cloth[1]] += 1
    for clo in hash_map.values():
        answer *= (clo + 1)
    return answer - 1
