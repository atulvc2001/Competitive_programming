class Solution {
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        HashMap<Integer,Integer> m  = new HashMap<Integer,Integer>();
        for(int num:arr){
            m.put(num, m.getOrDefault(num, 0)+1);
        }
        List<Integer> list = new ArrayList<Integer>(m.values());
        Collections.sort(list);
        for(int i=0;i<k;i++){
            if (list.get(0) == 1)
                list.remove(0);
            else 
                list.set(0, list.get(0)-1);
        }
        return list.size();
        
    }
}
