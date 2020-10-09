#include <algorithm>
#include <cctype>
#include <string>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        int size = s.length();
        
        int end = size-1;
        int start = 0;
        while(end > start){ //투포인터로 구현
            while(end >= 0 && !(isalpha(s[end]) || isdigit(s[end])))
                end--;
            while(start < size && !(isalpha(s[start]) || isdigit(s[start])))
                start++;
            
            if(end >= 0 && start < size){
                if(isalpha(s[end]) && isalpha(s[start]))
                    if(tolower(s[end]) != tolower(s[start]))
                        return false;
                if(isdigit(s[start]) && isdigit(s[end]))
                    if(s[start] != s[end])
                        return false;
                    
                if(isalpha(s[end]) && isdigit(s[start]))
                    return false;
                if(isalpha(s[start]) && isdigit(s[end]))
                    return false;
                
            }
            
            end--;
            start++;
        }//while
        
        return true;
    }
        
    
};
