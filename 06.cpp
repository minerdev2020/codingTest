#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>


using namespace std;

bool is_prime(int n) {
    if (n == 0 || n == 1) 
        return false;
    for (int i = 2; i <= sqrt(n); i++)
        if (n % i == 0) 
            return false;
    return true;
}

int solution(string numbers) {
    vector <int> allCase;
    vector <int> vec;
    int answer = 0;
    for (int i = 0; i < numbers.size(); i++) 
        vec.push_back(numbers[i] - '0');
    sort(vec.begin(), vec.end());
    
    do
    {
        for (int i = 0; i <= vec.size(); i++) {
            int temp = 0;
            for (int j = 0; j < i; j++) {
                temp = (temp * 10) + vec[j];
                allCase.push_back(temp);
            }
        }
    } while (next_permutation(vec.begin(), vec.end()));
    
    sort(allCase.begin(), allCase.end());
    allCase.erase(unique(allCase.begin(), allCase.end()), allCase.end());

    for (int i = 0; i < allCase.size(); i++)
        if (is_prime(allCase[i])) 
            answer++;
    return answer;
}
