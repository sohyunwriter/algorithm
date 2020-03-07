#include <stack>
using namespace std;

class MinStack {
public:
    /** initialize your data structure here. */
    // 두 개의 스택을 이용해 구현
    stack<int> s;
    stack<int> minS;
    
    MinStack() {
        
    }
    
    void push(int x) {
        s.push(x);
        if(minS.empty())
            minS.push(x);
        else{
            int pastMin = minS.top();
            if(x < pastMin)
                minS.push(x);
            else
                minS.push(pastMin);
        }
    }
    
    void pop() {
        s.pop();
        minS.pop();
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return minS.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
