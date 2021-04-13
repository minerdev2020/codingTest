#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;

    unordered_map<string, int> hash_map;
    for(int i = 0; i < phone_book.size(); i++)
        hash_map[phone_book[i]] = 1;

    for(int i = 0; i < phone_book.size(); i++) {
        string phone_number = "";
        for(int j = 0; j < phone_book[i].size(); j++) {
            phone_number += phone_book[i][j];
            if(hash_map[phone_number] && phone_number != phone_book[i]){
                answer = false; 
                return false;
            }
        }
    }
    return true;
}

#python
def solution(phone_book):
    for phone in phone_book:
        for other_phone in phone_book:
            if len(phone) >= len(other_phone):
                continue

            if hash(phone) == hash(other_phone[:len(phone)]):
                return False
    return True
