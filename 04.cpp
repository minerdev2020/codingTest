#include <algorithm>
#include <string>
#include <vector>

using namespace std;

bool compare(string a, string b)  //my answer
{
    int i = 0;
    while(1){
        if(a[i] > b[i])
            return true;
        if(a[i] < b[i])
            return false;
        i++;
        if(i > 2)
            return false;
        if(a.size() == i){
            if(b.size() == i)
                return false;
            else
                a += a;
        }
        if(b.size() == i){
            b += b;
        }
    }
}

/*bool compare(string a, string b)    //best answer
{
    if (b + a < a + b)
        return true;
    return false;
}*/

string solution(vector<int> numbers) {
    string answer = "";

    vector<string> strings;

    for (int i : numbers)
        strings.push_back(to_string(i));

    sort(strings.begin(), strings.end(), compare);

    for (auto iter = strings.begin(); iter < strings.end(); ++iter)
        answer += *iter;

    if (answer[0] == '0')
        answer = "0";

    return answer;
}
