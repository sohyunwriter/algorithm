#include <string>
#include <vector>

using namespace std;

//dfs
void dfs(vector<int> numbers, int& answer, int idx, int sum, int target){
    if(idx == numbers.size()){
        if(sum == target){
            answer++;
        }
        return;
    }
    dfs(numbers, answer, idx+1, sum+numbers[idx],target);
    dfs(numbers, answer, idx+1, sum-numbers[idx], target);
}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    dfs(numbers, answer, 0, 0, target);
    return answer;
}
