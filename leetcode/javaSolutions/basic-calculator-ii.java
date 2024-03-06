
public class Solution {
    public int calculate(String s) {
        int i = 0;
        int cur = 0, prev = 0, res = 0;
        char curOperation = '+';

        while (i < s.length()) {
            char curChar = s.charAt(i);

            if (Character.isDigit(curChar)) {
                while (i < s.length() && Character.isDigit(s.charAt(i))) {
                    cur = cur * 10 + (s.charAt(i) - '0');
                    i++;
                }

                i--;

                if (curOperation == '+') {
                    res += cur;
                    prev = cur;
                } else if (curOperation == '-') {
                    res -= cur;
                    prev = -cur;
                } else if (curOperation == '*') {
                    res -= prev;
                    res += prev * cur;
                    prev = cur * prev;
                } else {
                    res -= prev;
                    res += prev / cur;
                    prev = prev / cur;
                }
            
                cur = 0;
            } else if (curChar != ' ') {
                curOperation = curChar;
            }
            
            i++;
        }

        return res;
    }
}
