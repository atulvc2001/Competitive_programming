class Solution {
    public int titleToNumber(String columnTitle) {
        
        int cur = 0;

        for(int i = 0; i < columnTitle.length(); i++){
            cur = cur*26 + ((columnTitle.charAt(i) - 'A')+1);
        }
        System.out.println(cur);
        return cur;
    }
}
