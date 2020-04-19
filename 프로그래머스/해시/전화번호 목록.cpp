//https://sohyunwriter.tistory.com/134

#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    unordered_map<string, int> map;
    
    for(auto i : phone_book)
        ++map[i];
    
    for(int i = 0; i < phone_book.size(); i++){
        string number = "";
        for(int j = 0; j < phone_book[i].size(); j++){
            number += phone_book[i][j];
            if(map[number] > 0 && phone_book[i] != number)
                return false;
        }
    }
        
        
    return true;
}
