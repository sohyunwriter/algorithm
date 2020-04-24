#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> budgets, int M) {
    long long answer = 0;
    int n = budgets.size(); //지방의 수
    int start = 0;
    int end = budgets.size()-1;
    sort(budgets.begin(), budgets.end());
    long long sum = budgets[0];
    
    for(int i = 1; i < n; i++)
        sum += budgets[i];
    
    if(sum <= M)
        return budgets[n-1];
    
    //else
    int mid = 0;
    start = 0;
    end = budgets[budgets.size()-1];
    while(start <= end){
        mid = (start + end) / 2;
        long long msum = 0;
        for(int i = 0; i < budgets.size(); i++){
            if(budgets[i] < mid)
                msum += budgets[i];
            else{
                msum += (budgets.size() - i) * mid;
                break;
            }
        }
        
        if(msum <= M){
            answer = mid;
            start = mid + 1;
        }
        else
            end = mid - 1;
    }
    
    return answer;
}
