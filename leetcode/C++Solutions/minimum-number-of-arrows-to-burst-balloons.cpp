
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

/* 
 *
 * I think the below code is another way of writing the above solution but little bit more efficiently
#include <vector>
#include <algorithm>

class Solution {
public:
    int findMinArrowShots(std::vector<std::vector<int>>& points) {
        if (points.empty()) return 0;

        int arrows = 1;
        std::sort(points.begin(), points.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[1] < b[1];
        });

        int end = points[0][1];

        for (int i = 1; i < points.size(); ++i) {
            if (points[i][0] > end) {
                arrows++;
                end = points[i][1];
            }
        }

        return arrows;
    }
}; */
