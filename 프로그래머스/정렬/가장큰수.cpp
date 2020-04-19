//https://sohyunwriter.tistory.com/140

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(string a, string b){
    return a + b > b + a;
}

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> v;
    
    for(auto i:numbers){
        v.push_back(to_string(i));
    }
    sort(v.begin(), v.end(), compare);
    if(v[0] == "0"){ // {0, 0, 0, 0} -> "0"
        return "0";
    }
    for(auto i : v)
        answer += i;
    return answer;
}
