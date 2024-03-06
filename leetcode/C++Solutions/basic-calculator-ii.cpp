
#include <string>
#include <cctype>

class Solution {
public:
    int calculate(std::string s) {
        int i = 0;
        int cur = 0, prev = 0, res = 0;
        char cur_operation = '+';

        while (i < s.length()) {
            char cur_char = s[i];

            if (isdigit(cur_char)) {
                while (i < s.length() && isdigit(s[i])) {
                    cur = cur * 10 + (s[i] - '0');
                    i++;
                }

                i--;

                if (cur_operation == '+') {
                    res += cur;
                    prev = cur;
                } else if (cur_operation == '-') {
                    res -= cur;
                    prev = -cur;
                } else if (cur_operation == '*') {
                    res -= prev;
                    res += prev * cur;
                    prev = cur * prev;
                } else { 
                    res -= prev;
                    res += prev / cur;
                    prev = prev / cur;
                }
            
                cur = 0;
            } else if (cur_char != ' ') {
                cur_operation = cur_char;
            }
            
            i++;
        }

        return res;
    }
};
