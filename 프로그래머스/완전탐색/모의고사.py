#include <string>
#include <vector>
#include <algorithm>

// 문제: https://programmers.co.kr/learn/courses/30/lessons/42840

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> ans;
    vector<int> answer(3);
    int a[5] = {1, 2, 3, 4, 5};
    int b[8] = {2, 1, 2, 3, 2 ,4, 2, 5};
    int c[10] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    
    
    for(int i = 0; i < answers.size(); i++){
        int num = answers[i];
        if(num == a[i % 5])
            answer[0]++;
        if(num == b[i%8])
            answer[1]++;
        if(num == c[i%10])
            answer[2]++;
    }
    
    int maxn = 0;
    for(int i = 0; i < answer.size(); i++){
        if(answer[i] > maxn)
            maxn = answer[i];
    }    
    
    if(maxn != 0){
        for(int i = 0; i < answer.size(); i++){
            if(answer[i] == maxn)
                ans.push_back(i+1);
        }
    }
    
    return ans;
}
