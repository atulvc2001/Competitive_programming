
#include <vector>
#include <string>

class Solution {
public:
    std::vector<std::string> summaryRanges(std::vector<int>& nums) {
        std::vector<std::string> op;
        if (nums.empty()) {
            return op;
        }

        int s = 0, e = 0;

        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] != nums[i - 1] + 1) {
                if (s == e) {
                    op.push_back(std::to_string(nums[s]));
                } else {
                    op.push_back(std::to_string(nums[s]) + "->" + std::to_string(nums[e]));
                }
                s = e = i;
            } else {
                e = i;
            }
        }

        if (s == e) {
            op.push_back(std::to_string(nums[s]));
        } else {
            op.push_back(std::to_string(nums[s]) + "->" + std::to_string(nums[e]));
        }

        return op;
    }
};
