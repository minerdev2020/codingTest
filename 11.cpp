#include <string>
#include <vector>
#include <algorithm>
using namespace std;
vector<vector<string>> answerlist;
 
void dfs(vector<vector<string>> &tickets, vector<pair<int, int>> &useCheck, string from, int count) {
    if (count == tickets.size()) {
        vector<string> answer;
        vector<pair<int, int>> temp = useCheck;
        sort(temp.begin(), temp.end());
        for (auto a : temp)        answer.push_back(tickets[a.second][0]);
        answer.push_back(tickets[temp[temp.size() - 1].second][1]);
        answerlist.push_back(answer);
        return;
    }
    for (int i = 0; i < tickets.size(); i++) {
        if (useCheck[i].second == -1 && tickets[i][0] == from) {
            useCheck[i] = { count, i};
            dfs(tickets, useCheck, tickets[i][1], count + 1);
            useCheck[i] = { 0, -1 };
        }
    }
}
 
vector<string> solution(vector<vector<string>> tickets) {
    vector<pair<int, int>> useCheck(tickets.size(), { 0 , -1 });
    dfs(tickets, useCheck, "ICN", 0);
    sort(answerlist.begin(), answerlist.end());
    return answerlist[0];
}
