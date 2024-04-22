
#include <vector>
#include <set>

class Solution {
public:
    bool containsNearbyDuplicate(std::vector<int>& nums, int k) {
        int L = 0;
        int R = 0;

        std::set<int> numSet;

        while (R < nums.size()) {
            if (R - L > k) {
                numSet.erase(nums[L]);
                L += 1;
            }

            if (numSet.find(nums[R]) != numSet.end()) { // Fix the condition
                return true;
            }

            numSet.insert(nums[R]);
            R += 1;
        }

        return false;
    }
};
