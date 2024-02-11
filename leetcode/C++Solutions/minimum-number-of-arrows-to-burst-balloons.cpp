
#include <vector>
#include <algorithm>

class Solution {
public:
    int findMinArrowShots(std::vector<std::vector<int>>& points) {
        // Sort intervals based on start points
        std::sort(points.begin(), points.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[0] < b[0];
        });

        int balloons = points.size();
        int i = 1;
        int r = points[0][1];
        int l = points[0][0];

        while (i < points.size()) {
            if (r < points[i][0]) {
                l = points[i][0];
                r = points[i][1];
                i++;
                continue;
            }

            l = std::max(l, points[i][0]);
            r = std::min(r, points[i][1]);
            i++;
            balloons--;
        }

        return balloons;
    }
};

