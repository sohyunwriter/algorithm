//https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

// not use STL

class Solution {
public:
    int lowerbound(vector<int>& v, int target){
        int start = 0;
        int end = v.size();
        int mid;
        
        while(start < end){
            mid = (start+end) / 2;
            if(v[mid] >= target)
                end = mid;
            else
                start = mid + 1;
        }
        
        return end;
    }
    
    int upperbound(vector<int>& v, int target){
        int start = 0;
        int end = v.size();
        int mid;
        
        while(start < end){
            mid = (start+end) / 2;
            if(v[mid] > target)
                end = mid;
            else
                start = mid + 1;
        }
        
        return end;
        
    }
    
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> answer;
        
        int lb = lowerbound(nums, target);
        int ub = upperbound(nums, target);
        
        //lowerbound
        if(lb >= nums.size()){
            lb = -1;
        }
        else if(nums[lb] != target){
            lb = -1;
        }
        
        //upperbound
        if(ub == 0)
            ub = -1;
        else if(nums[ub-1] == target)
            ub--;
        else
            ub = -1;
        
        answer.push_back(lb);
        answer.push_back(ub);
        
        return answer;
    }
    
    
};
