
#include <vector>

class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int ROWS = board.size();
        int COLS = board[0].size();

        auto countNeighbours = [&](int r, int c) {
            int nei = 0;
            for (int i = r - 1; i <= r + 1; ++i) {
                for (int j = c - 1; j <= c + 1; ++j) {
                    if ((i == r && j == c) || i < 0 || j < 0 || i == ROWS || j == COLS) {
                        continue;
                    }
                    if (board[i][j] == 1 || board[i][j] == 3) {
                        nei++;
                    }
                }
            }
            return nei;
        };

        for (int r = 0; r < ROWS; ++r) {
            for (int c = 0; c < COLS; ++c) {
                int nei = countNeighbours(r, c);
                if (board[r][c]) {
                    if (nei == 2 || nei == 3) {
                        board[r][c] = 3;
                    }
                } else {
                    if (nei == 3) {
                        board[r][c] = 2;
                    }
                }
            }
        }

        for (int r = 0; r < ROWS; ++r) {
            for (int c = 0; c < COLS; ++c) {
                if (board[r][c] == 1) {
                    board[r][c] = 0;
                } else if (board[r][c] == 2 || board[r][c] == 3) {
                    board[r][c] = 1;
                }
            }
        }
    }
};
