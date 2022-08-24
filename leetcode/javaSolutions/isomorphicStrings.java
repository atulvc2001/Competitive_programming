class Solution {
    public boolean isIsomorphic(String s, String t) {
        HashMap<Character,Character> map = new HashMap<Character,Character>();
        for(int i=0;i<s.length();i++){
            if (map.containsKey(s.charAt(i))){
                if (map.get(s.charAt(i))!=t.charAt(i))
                    return false;
            }
            else{
                map.put(s.charAt(i),t.charAt(i));
            }
        }
        HashMap<Character,Character> Map = new HashMap<Character,Character>();
        for(int i=0;i<s.length();i++){
            if (Map.containsKey(t.charAt(i))){
                if (Map.get(t.charAt(i))!=s.charAt(i))
                    return false;
            }
            else{
                Map.put(t.charAt(i),s.charAt(i));
            }
        }
        return true;
    }
}
