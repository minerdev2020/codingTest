#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    unordered_map <string, int> sum_map;
    unordered_map <string, pair<int, int>> first_map;
    unordered_map <string, pair<int, int>> second_map;
    vector<pair<int, string>> gen_array;
    for(int i = 0; i < genres.size(); i++){
        sum_map[genres[i]] += plays[i];
        if(plays[i] > first_map[genres[i]].second){
            second_map[genres[i]].first = first_map[genres[i]].first;
            second_map[genres[i]].second = first_map[genres[i]].second;
            first_map[genres[i]].first = i;
            first_map[genres[i]].second = plays[i];
        }
        else if(plays[i] > second_map[genres[i]].second){
            second_map[genres[i]].first = i;
            second_map[genres[i]].second = plays[i];
        }      
    }
    for(auto it = sum_map.begin(); it != sum_map.end(); it++)
        gen_array.push_back(pair<int, string>(it->second, it->first));
    sort(gen_array.begin(), gen_array.end(), greater<>());
    for(auto it = gen_array.begin(); it != gen_array.end(); it++){
        if(first_map[it->second].second != 0)
            answer.push_back(first_map[it->second].first);
        if(second_map[it->second].second != 0)
            answer.push_back(second_map[it->second].first);
    }
    return answer;
}
