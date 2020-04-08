#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    unordered_map<string, int> map;
    
    for(int i = 0; i < clothes.size(); i++)
        ++map[clothes[i][1]];
    
    for(auto pair : map)
        answer *= (pair.second+1);
        
    answer--;
    
    return answer;
}
