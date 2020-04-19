//https://sohyunwriter.tistory.com/138

#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    vector<int> a;
    
    for(int i = 0; i < commands.size(); i++){
        a = array;
        sort(a.begin() + commands[i][0]-1, a.begin()+commands[i][1]);
        answer.push_back(a[commands[i][0] + commands[i][2] -2]);
    }
    return answer;
}
