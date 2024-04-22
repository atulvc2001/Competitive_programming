class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> ans(temperatures.size(), 0);
        stack<int> monostack;

        for (int i = temperatures.size() - 1; i >= 0; --i) {
            while (!monostack.empty() && temperatures[monostack.top()] <= temperatures[i]) {
                monostack.pop();
            }

            if (!monostack.empty()) {
                ans[i] = monostack.top() - i;
            }

            monostack.push(i);
        }

        return ans;
    }
};
