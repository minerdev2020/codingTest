#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

long long solution(int n, vector<int> times) {
    sort(times.begin(), times.end());

    long long left = (long long)times[0];
    long long right = (long long)times[0] * n;
    long long answer = right;
    while(left <= right){
        long long mid = (right + left) / 2;
        long long pass = 0;
        for(int i = 0; i < times.size(); i++)
            pass += mid / (long long)times[i];
        if(pass <= n){
            left = mid + 1;
            if(answer <= mid)
                answer = mid;
        }
        else
            right = mid - 1;

    }
    return answer;
}
