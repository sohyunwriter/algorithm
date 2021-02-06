#include <string>
#include <vector>
#include <algorithm>

using namespace std;

//연속 개수
bool isPossible(vector<int> stones, int num, int k){
    int count = 0;
    
    for(int i = 0; i < stones.size(); i++){
        if(stones[i] - num <= 0)
            count++;
        else
            count = 0;
        if(count >= k)
            return false;
    }
    return true;
}

int solution(vector<int> stones, int k) { 
    //징검다리 건너는 사람 수
    int first = 1;
    int last = *max_element(stones.begin(), stones.end());

    // binary search
    while(first <= last){
        int mid = (first + last) / 2;
        if(isPossible(stones, mid, k)){ //더 건널 수 있음
            first = mid + 1;
        } else
            last = mid - 1;
    }
   
    return first;
}
