
class MinStack {
public:
    stack<int> arr;       // Regular stack for elements.
    stack<int> min_arr;   // Stack for maintaining the minimum at each step.

    MinStack() {
        // Constructor.
    }
    
    void push(int val) {
        // Push the value onto the regular stack.
        arr.push(val);
        // Update the value to be pushed onto the minimum stack, considering the current minimum.
        if (!min_arr.empty()) {
            val = min(val, min_arr.top());
        }
        // Push the updated value onto the minimum stack.
        min_arr.push(val);
    }
    
    void pop() {
        // Pop elements from both stacks to maintain synchronization.
        arr.pop();
        min_arr.pop();
    }
    
    int top() {
        // Retrieve the top element from the regular stack.
        return arr.top();
    }
    
    int getMin() {
        // Retrieve the top element from the minimum stack, representing the current minimum.
        return min_arr.top();
    }
};
