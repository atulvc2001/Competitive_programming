class Solution {
public:
    int titleToNumber(string columnTitle) {
        int cur = 0;

        for(int i = 0; i < columnTitle.length(); i++){
            cur = cur * 26 + (columnTitle[i] - 'A' +1);
        }
        
        return cur;
    }
};
